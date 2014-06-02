'''Algorithms for calculating scores'''

from collections import OrderedDict
import random

from django.core.urlresolvers import reverse
from scipy.stats import norm

from boundaryservice.models import Boundary
from healthdata.utils import fake_boundary
from data.models import Census


class BaseAlgorithm(object):
    def __init__(self, node, metric):
        self.node = node
        self.metric = metric

    def boundaries_for_location(self, location):
        '''
        Generate boundaries for a (lon, lat) location

        Return should be a iterable of Boundary objects in preferred order
        '''
        raise NotImplementedError('boundaries_for_location is not implemented')

    def source_data_for_boundary(self, boundary):
        '''
        Return source data for a boundary

        Return should be a source data instance with appropriate data,
        or None if no data for the boundary.
        '''
        raise NotImplementedError(
            'source_data_for_boundary is not implemented')

    def score(self, source_data):
        '''
        Score an item of source data

        Return should be a dictionary with at least:
        {
            'summary': {
                'score': (the score, 0.0 to 1.0),
                'value': (the raw value),
                'value_type': (the type of the value, such as 'percent'),
                'description': (a short description of the metric),
            }
        }
        It can include more summary items.
        It can also include a 'detail' dictionary with additional information

        TODO: more required details
        '''
        raise NotImplementedError('score is not implemented')

    def source_data_for_location(self, location):
        '''Generate source data for a (lon, lat) location'''
        for boundary in self.boundaries_for_location(location):
            source_data = self.source_data_for_boundary(boundary)
            if source_data:
                yield source_data

    def boundary_path(self, boundary):
        '''Return the path to the boundary API endpoint'''
        return reverse('api:boundary', kwargs={'slug': boundary.slug})

    def detail_path(self, boundary):
        '''Return the path to the metric detail API endpoint'''
        return reverse(
            'api:metric-detail', kwargs={
                'boundary_slug': boundary.slug, 'node_slug': self.node.slug})

    def calculate(self, source_data):
        '''
        Calculate a metric dictionary from valid source data

        Return is a dictionary with three items: summary, detail, and boundary
        '''
        calculation = self.score(source_data)
        boundary = source_data.boundary
        calculation.setdefault('detail', {}).update({
            'path': self.detail_path(boundary),
        })
        calculation.setdefault('boundary', {}).update({
            'path': self.boundary_path(boundary),
        })
        return calculation

    def calculate_by_boundary(self, boundary):
        '''
        Calculate a metric dictionary for a boundary

        If there is no data for a boundary, None is returned
        '''
        source_data = self.source_data_for_boundary(boundary)
        if source_data:
            return self.calculate(source_data)
        else:
            return None

    def calculate_by_location(self, location):
        '''
        Calculate a metric dictionary for a (lon, lat) location

        If there is no data for a location, None is returned
        '''
        for source_data in self.source_data_for_location(location):
            calculation = self.calculate(source_data)
            if calculation:
                return calculation
        return None


class PlaceholderAlgorithm(BaseAlgorithm):
    '''Placeholder for data that we plan to import in the future'''

    class PlaceholderData(object):
        '''Randomized data that is consistant for a boundary/node combo'''
        def __init__(self, boundary, seed):
            self.boundary = boundary
            random.seed(seed)
            self.score = random.randint(0, 100) / 100.0
            self.value = random.randint(0, 100) / 100.0

    def boundary_path(self, boundary):
        return reverse(
            'api:fake-boundary', kwargs={'slug': boundary.slug})

    def boundaries_for_location(self, location):
        '''Return a fake Boundary, roughly 1/2 sq. mile'''
        return [fake_boundary(location, 2)]

    def source_data_for_boundary(self, boundary):
        seed = self.detail_path(boundary)
        return self.PlaceholderData(boundary, seed)

    def score(self, source_data):
        score_text = (
            "We don't have data for {node.label} yet, but studies show it"
            " has an impact on the health of a community. Do you know about"
            " a data source? <a href='{feedback_url}'>Tell us about it</a>."
        ).format(node=self.node, feedback_url='#')
        return {
            'summary': OrderedDict((
                ("score", source_data.score),
                ("value", source_data.value),
                ("value_type", "percent"),
                ("description", self.metric.description),
            )),
            'detail': OrderedDict((
                ("score_text", score_text),
            )),
            'boundary': OrderedDict((
                ("label", "Future Data Placeholder"),
                ("type", "Placeholder"),
            )),
        }


class CensusPercentAlgorithm(BaseAlgorithm):
    '''
    Algorithm for census-based calcuations of ratio vs. the state average
    '''
    # Default boundary set order
    boundary_set_slugs = (
        'census-block-groups',
        'census-tracts',
        'counties',
        'states',)

    def source_data_for_boundary(self, boundary):
        '''Get census data where the total population is not 0'''
        total_fields, _ = self.get_fields()
        empty_totals = {field: 0 for field in total_fields}
        try:
            source_data = Census.objects.exclude(
                **empty_totals).get(boundary=boundary)
        except Census.DoesNotExist:
            return None
        else:
            return source_data

    def boundaries_for_location(self, location):
        '''Generate census boundaries containing the point, smallest first'''
        wkt = 'POINT({} {})'.format(*location)
        for set_slug in self.boundary_set_slugs:
            try:
                boundary = Boundary.objects.get(
                    set__slug=set_slug, shape__contains=wkt)
            except Boundary.DoesNotExist:
                pass
            else:
                yield boundary

    def score(self, source_data):
        '''
        Score based on the ratio vs the state ratio

        For example, the metric 'Percentage on Food Stamps' comes from Census
        table B19058.  The total households is item 1, and the count on food
        stamps or other assistance is item 2.  The percent for any one census
        tract is the count divided by the total.  The score is the percent of
        census tracts across the state that have a lower percentage on food
        stamps, which can be calculated using the cumulative distribution
        function (CDF) with the tract's ratio, the state average, and the
        state standard deviation.  The last two can be pre-calcuated.
        '''
        total_fields, target_fields = self.get_fields()
        total = sum([getattr(source_data, f) for f in total_fields])
        target = sum([getattr(source_data, f) for f in target_fields])
        percent = float(target) / float(total)
        avg, std_dev, better_sign = self.get_stats(source_data)
        cdf = norm.cdf(percent, avg, std_dev)
        if better_sign >= 0:
            score = cdf
        else:
            score = 1.0 - cdf
        return {
            'summary': OrderedDict((
                ("score", round(score, 3)),
                ("value", round(percent, 3)),
                ("average", avg),
                ("std_dev", std_dev),
                ("value_type", "percent"),
                ("description", self.metric.description),
            )),
            'detail': OrderedDict((
            )),
            'boundary': OrderedDict((
                ("label", source_data.boundary.display_name),
                ("type", source_data.boundary.kind),
                ("external_id", source_data.boundary.external_id)
            )),
        }

    def get_fields(self):
        '''
        Return data field names on source data

        Returns a two-element tuple:
        - total_fields - Names of fields with population totals
        - target_fields - Names of fields with target group counts
        '''
        pattern = self.table + '_{:03}E'
        total_fields = [pattern.format(f) for f in self.total_column_ids]
        target_fields = [pattern.format(f) for f in self.target_column_ids]
        return total_fields, target_fields

    def get_stats(self, source_data):
        '''
        Return population statistics

        Return is a 3-element tuple:
        - average - The average value for the population
        - standard deviation - The standard deviation for the population
        - better_sign - Positive if higher than average is good, negative if
          lower than average is good.
        '''
        raise NotImplementedError('get_stats not implemented')


class FoodStampAlgorithm(CensusPercentAlgorithm):
    '''Score based on percentage of households on food stamps/assistance'''

    table = 'B19058'
    total_column_ids = (1,)
    target_column_ids = (2,)

    def get_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.138
        std_dev = 0.106
        better_sign = -1
        return average, std_dev, better_sign


class PercentPovertyAlgorithm(CensusPercentAlgorithm):
    '''Score based on percentage of households under povery level'''

    table = 'B17001'
    total_column_ids = (1,)
    target_column_ids = (2,)

    def get_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.166
        std_dev = 0.118383
        better_sign = -1
        return average, std_dev, better_sign


def boundaries(point):
    raise Exception('Convert to new way')


def boundary_dict(boundary):
    raise Exception('Convert to new way')


class PercentUnemploymentAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = (
            'B23001_001E', 'B23001_008E', 'B23001_015E',
            'B23001_022E', 'B23001_029E', 'B23001_036E',
            'B23001_043E', 'B23001_050E', 'B23001_057E',
            'B23001_064E', 'B23001_071E', 'B23001_076E',
            'B23001_081E', 'B23001_086E', 'B23001_094E',
            'B23001_101E', 'B23001_108E', 'B23001_115E',
            'B23001_122E', 'B23001_129E', 'B23001_136E',
            'B23001_143E', 'B23001_150E', 'B23001_157E',
            'B23001_162E', 'B23001_167E', 'B23001_172E',
        )
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B23001_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(
            boundary=boundary).exclude(B23001_001E=0).values_list(
                *list_of_rows).first()
        boundary = boundary_dict(data.boundary)
        citation = OrderedDict((
            ('path', '/api/citation/census/B23001/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B23001'),
        ))
        data_list = list(new_data)
        total = data_list.pop(0)
        total_unemployed = sum(data_list)
        percent = total_unemployed / float(total)
        state_avg = 0.04193
        state_std_dev = 0.0266
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)
        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentSingleParentAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B09002_001E', 'B09002_008E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B09002_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B09002_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', '/api/citation/census/B09002/'),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B09002'),
        ))

        total = data[0]
        total_single_parent = data[1]
        percent = total_single_parent / float(total)
        state_avg = 0.452998
        state_std_dev = 0.1657150
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentIncomeHousingCostAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B25091_001E', 'B25070_001E', 'B25070_008E',
            'B25070_009E', 'B25070_010E', 'B25091_009E',
            'B25091_010E', 'B25091_011E', 'B25091_020E',
            'B25091_021E', 'B25091_022E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B25091_001E=0, B25070_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B25091_001E=0, B25070_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/('B25091', 'B25070')/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', ('B25091', 'B25070')),
        ))

        total = data[0] + data[1]
        total_renter_gradual = data[2]/float(4) + data[3]/float(2) + data[4]
        total_mortgaged_owner = data[5]/float(4) + data[6]/float(2) + data[7]
        total_unmortgaged_owner = (
            data[8]/float(4) + data[9]/float(2) + data[10])
        percent = (
            total_renter_gradual + total_mortgaged_owner +
            total_unmortgaged_owner)/float(total)
        state_avg = 0.1544959
        state_std_dev = 0.0867039
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentHighSchoolGraduatesAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B15002_001E', 'B15002_011E', 'B15002_012E',
            'B15002_013E', 'B15002_014E', 'B15002_015E',
            'B15002_016E', 'B15002_017E', 'B15002_018E',
            'B15002_028E', 'B15002_029E', 'B15002_030E',
            'B15002_031E', 'B15002_032E', 'B15002_033E',
            'B15002_034E', 'B15002_035E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B15002_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B15002_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B15002/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B15002'),
        ))

        data_list = list(data)
        total = data_list.pop(0)
        high_school_grads = sum(data_list)
        percent = high_school_grads/float(total)
        state_avg = 0.861836
        state_std_dev = 0.096739
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentDivorcedMarriageAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B12001_001E', 'B12001_003E', 'B12001_009E',
            'B12001_012E', 'B12001_018E', 'B12001_005E',
            'B12001_014E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B12001_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B12001_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B12001/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B12001'),
        ))

        total = data[0] - data[1] - data[2] - data[3] - data[4]
        total_currently_good_marriage = data[5] + data[6]
        percent = total_currently_good_marriage/float(total)
        state_avg = 0.735492
        state_std_dev = 0.139789
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentOvercrowdingAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B25014_001E', 'B25014_003E', 'B25014_004E',
            'B25014_005E', 'B25014_006E', 'B25014_007E',
            'B25014_009E', 'B25014_010E', 'B25014_011E',
            'B25014_012E', 'B25014_013E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B25014_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B25014_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B25014/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B25014'),
        ))

        data_list = list(data)
        total = data_list[0]
        decent_housing = (data_list[2] + data_list[7])/8.0
        crowded_housing = (data_list[3] + data_list[8])/4.0
        cramped_housing = (data_list[4] + data_list[9])/2.0
        bad_housing = float(data_list[5] + data_list[10])
        total_negative_housing = (
            decent_housing + crowded_housing + cramped_housing + bad_housing)
        percent = total_negative_housing/float(total)
        state_avg = 0.040577
        state_std_dev = 0.014887
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentGeographicMobilityAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B07013_001E', 'B07013_004E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B07013_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B07013_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B07013/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B07013'),
        ))

        total = data[0]
        same_house_year_ago = data[1]
        different_house_year_ago = total - same_house_year_ago
        percent = different_house_year_ago/float(total)
        state_avg = 0.168965
        state_std_dev = 0.09219
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))

        return score, citation, boundary


class PercentCollegeGraduateAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B15003_001E', 'B15003_021E', 'B15003_022E',
            'B15003_023E', 'B15003_024E', 'B15003_025E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B15003_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B15003_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B15003/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B15003'),
        ))

        data_list = list(data)
        total = data_list.pop(0)
        college_grads = sum(data_list)
        percent = college_grads/float(total)
        state_avg = 0.301417
        state_std_dev = 0.153007
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentBadCommuteTimesAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B08303_001E', 'B08303_008E', 'B08303_009E',
            'B08303_010E', 'B08303_011E', 'B08303_012E',
            'B08303_013E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B08303_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B08303_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B08303/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B08303'),
        ))
        total = data[0]
        bad_commutes = (
            data[1]/16.0 + data[2]/8.0 + data[3]/4.0 + data[4]/2.0 +
            data[5] + data[6])
        percent = bad_commutes/float(total)
        state_avg = 0.082964
        state_std_dev = 0.059340889
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentImproperKitchenFacilitiesAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B25052_001E', 'B25052_003E'
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B25052_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B25052_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B25052/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B25052'),
        ))
        total = data[0]
        improper_facilities = sum(data[1:])
        percent = improper_facilities/float(total)
        state_avg = 0.00976313
        state_std_dev = 0.01802429
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentImproperPlumbingAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B25048_001E', 'B25048_003E'
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B25048_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B25048_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B25048/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B25048'),
        ))
        total = data[0]
        improper_plumbing = sum(data[1:])
        percent = improper_plumbing/float(total)
        state_avg = 0.00572503
        state_std_dev = 0.0109313
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary


class PercentLowValueHousingAlgorithm(BaseAlgorithm):
    def calculate(self, point):
        list_of_rows = [
            'B25075_001E', 'B25075_002E', 'B25075_003E',
            'B25075_004E', 'B25075_005E', 'B25075_006E',
            'B25075_007E', 'B25075_008E', 'B25075_009E',
            'B25075_010E', 'B25075_011E', 'B25075_012E',
            'B25075_013E', 'B25075_014E', 'B25075_015E',
        ]
        for boundary in boundaries(point):
            try:
                data = Census.objects.filter(boundary=boundary).exclude(
                    B25075_001E=0).first()
            except Census.DoesNotExist:
                pass
            else:
                break
        new_data = Census.objects.filter(boundary=boundary).values_list(
            *list_of_rows).exclude(B25075_001E=0).first()
        boundary = boundary_dict(data.boundary)
        data = new_data
        citation = OrderedDict((
            ('path', "/api/citation/census/B25075/",),
            ('label', 'Census 5 Year Summary, 2008-2012'),
            ('year', 2012),
            ('type', 'percent'),
            ('id', 'B25075'),
        ))
        total = data[0]
        low_value = sum((
            data[1], data[2]/2.0, data[3]/2.0, data[4]/4.0,
            data[5]/4.0, data[6]/8.0, data[7]/8.0, data[8]/16.0, data[9]/32.0,
            data[10]/48.0, data[11]/64.0, data[12]/80.0, data[13]/96.0,
            data[14]/128.0))
        percent = low_value/float(total)
        state_avg = 0.0575880
        state_std_dev = 0.057490381
        score = 1.0 - norm.cdf(percent, state_avg, state_std_dev)

        score = OrderedDict((
            ("score", round(score, 3)),
            ("value", round(percent, 3)),
            ("average", state_avg),
            ("std_dev", state_std_dev),
            ("value_type", "percent"),
            ("description", self.metric.description),
            ("citation_path", citation['path']),
            ("boundary_path", boundary['path']),
        ))
        return score, citation, boundary
