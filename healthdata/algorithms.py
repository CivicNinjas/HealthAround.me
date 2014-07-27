'''Algorithms for calculating scores'''

from collections import OrderedDict
import random

from django.core.urlresolvers import reverse
from scipy.stats import norm
import markdown

from boundaryservice.models import Boundary
from healthdata.utils import fake_boundary
from data.models import Census, Dartmouth, Ers


class AlgorithmCache(object):
    '''Data that gets used repeatedly by algorithm calculations'''

    def __init__(self):
        self.location = None
        self.boundary = None
        self.boundaries = {}
        self.data = {}

    def get_boundary(self, location, boundary_set_slug):
        '''Get the boundary by location and boundary set slug'''

        # If location changed, clear the cache
        if self.location:
            if location != self.location:
                self.boundaries = {}
                self.location = location
        else:
            self.location = location

        # If needed, load the boundaries
        if not self.boundaries:
            wkt = 'POINT({} {})'.format(*location)
            boundaries = Boundary.objects.filter(
                shape__contains=wkt).select_related('set')
            for boundary in boundaries:
                self.boundaries[boundary.set.slug] = boundary
            self.boundaries['fake_2'] = fake_boundary(location, 2)

        # Return the boundary
        return self.boundaries.get(boundary_set_slug)

    def get_data(self, klass, boundary):
        '''Get data by boundary'''

        # Return the data
        boundaries = self.data.setdefault(klass.__name__, {})
        if boundary.id not in boundaries:
            try:
                data = klass.objects.get(boundary=boundary)
            except klass.DoesNotExist:
                data = None
            boundaries[boundary.id] = data
        return boundaries[boundary.id]


class BaseAlgorithm(object):
    '''
    Basic methods used by all algorithms

    Algorithms are used to score a metric by location.  This location
    can be determined by a boundary, or by a point (which is used to
    pick from the available boundaries)
    '''

    def __init__(self, node, metric, cache):
        self.node = node
        self.metric = metric
        self.cache = cache

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

    def source_data_for_boundary(self, boundary):
        '''
        Return source data for a boundary

        Return should be a source data instance with appropriate data,
        or None if no data for the boundary.
        '''
        raise NotImplementedError(
            'source_data_for_boundary is not implemented')

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

    def source_data_for_location(self, location):
        '''Generate source data for a (lon, lat) location'''
        for boundary in self.boundaries_for_location(location):
            source_data = self.source_data_for_boundary(boundary)
            if source_data:
                yield source_data

    def boundaries_for_location(self, location):
        '''
        Generate boundaries for a (lon, lat) location

        Return should be a iterable of Boundary objects in preferred order
        '''
        raise NotImplementedError('boundaries_for_location is not implemented')

    def calculate(self, source_data):
        '''
        Calculate a metric dictionary from valid source data

        Return is a dictionary with three items: summary, detail, and boundary
        '''
        calculation = self.score(source_data)
        boundary = source_data.boundary
        calculation.setdefault('detail', {}).update(
            self.expanded_detail(source_data, calculation))
        calculation.setdefault('boundary', {}).update({
            'path': self.boundary_path(boundary),
        })
        return calculation

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
        '''
        raise NotImplementedError('score is not implemented')

    def boundary_path(self, boundary):
        '''Return the path to the boundary API endpoint'''
        return reverse('api:boundary', kwargs={'slug': boundary.slug})

    def detail_path(self, boundary):
        '''Return the path to the metric detail API endpoint'''
        return reverse(
            'api:metric-detail', kwargs={
                'boundary_slug': boundary.slug, 'node_slug': self.node.slug})

    def expanded_detail(self, source_data, score):
        '''
        Extract data from metric.params to detail

        Special keys:
        stats - not added to detail
        more_data - List of dicts, expecting:
            type: 'census_reporter'
            table: A census table like B17001
            text: Link text like 'View on CensusReporter.org'
        '''
        boundary = source_data.boundary
        cr_prefix = {
            'Census Block Group': '15000US',
            'Census Tract': '14000US',
            'County': '05000US',
            'State': '04000US',
        }
        detail = {
            'path': self.detail_path(source_data.boundary)
        }
        params = self.metric.params or {}
        md = markdown.Markdown()
        for key, val in params.items():
            if key == 'stats':
                # Handled by get_stats
                pass
            elif key == 'more_data':
                detail['more_data'] = []
                for item in val:
                    out = item.copy()
                    mtype = item['type']
                    table = item['table']
                    text = item['text']
                    assert mtype == 'census_reporter'
                    link_fmt = (
                        'http://censusreporter.org/data/table/?table={table}'
                        '&geo_ids={geo_id}&primary_geo_id={geo_id}')
                    try:
                        geo_id = (
                            cr_prefix[boundary.kind] + boundary.external_id)
                    except KeyError:
                        geo_id = '04000US40'  # Oklahoma
                    out['link'] = link_fmt.format(
                        table=table, geo_id=geo_id)
                    out['markdown'] = "[{}]({})".format(text, out['link'])
                    out['html'] = md.convert(out['markdown'])
                    detail['more_data'].append(out)
            elif key == 'references':
                detail['references'] = []
                for item in val:
                    out = item.copy()
                    title = item['title']
                    publisher = item['publisher']
                    date = item['date']
                    link = item['link']
                    out['markdown'] = (
                        "[{}]({}), {}, {}".format(
                            title, link, publisher, date))
                    out['html'] = md.convert(out['markdown'])
                    detail['references'].append(out)
            elif key == 'score_md_fmt':
                items = {
                    'boundary': boundary.display_name,
                    'domain': 'Oklahoma',
                }
                raw_value = score['summary'].get('value')
                raw_average = score['summary'].get('average')
                raw_score = score['summary'].get('score')
                if (raw_value is None or raw_average is None or
                        raw_score is None):
                    continue
                assert score['summary']['value_type'] == 'percent'
                items['value'] = "{:.0%}".format(raw_value)
                items['average'] = "{:.0%}".format(raw_average)
                if raw_score >= .5:
                    items['rel'] = 'top {:.0%}'.format(1 - raw_score)
                else:
                    items['rel'] = 'bottom {:.0%}'.format(raw_score)
                out = {'markdown': val.format(**items)}
                out['html'] = md.convert(out['markdown'])
                detail['score_text'] = out
            elif key == 'why_md_fmt':
                detail['why_text'] = {
                    'markdown': val,
                    'html': md.convert(val),
                }
            else:
                # Add everything else to detail as is
                detail[key] = val
        return detail


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
        return [self.cache.get_boundary(location, 'fake_2')]

    def source_data_for_boundary(self, boundary):
        seed = self.detail_path(boundary)
        return self.PlaceholderData(boundary, seed)

    def score(self, source_data):
        feedback_url = "http://healtharound.me/#/feedback"
        score_md = (
            "We are still working on aggregating data for {node.label}. This"
            " data will be made available as time and funding allows. Do you"
            " know of another data source we should be aware of?"
            " [Tell us about it]({feedback_url})."
        ).format(node=self.node, feedback_url=feedback_url)

        return {
            'summary': OrderedDict((
                ("score", source_data.score),
                ("value", source_data.value),
                ("value_type", "percent"),
                ("description", self.metric.description),
            )),
            'detail':  OrderedDict((
                ("score_text", {
                    'markdown': score_md,
                    'html': markdown.markdown(score_md),
                }),
            )),
            'boundary': OrderedDict((
                ("label", "Future Data Placeholder"),
                ("type", "Placeholder"),
            )),
        }


class PercentAlgorithm(BaseAlgorithm):

    def local_percent(self, source_data):
        raise NotImplementedError('local_percent not implemented')

    def boundaries_for_location(self, location):
        '''Generate boundaries containing the point, smallest first'''
        for set_slug in self.boundary_set_slugs:
            boundary = self.cache.get_boundary(location, set_slug)
            if boundary:
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
        percent = self.local_percent(source_data)
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
            'detail': {},
            'boundary': OrderedDict((
                ("label", source_data.boundary.display_name),
                ("type", source_data.boundary.kind),
                ("external_id", source_data.boundary.external_id)
            )),
        }

    def get_stats(self, source_data):
        '''
        Return population statistics from the metric, or the default stats
        '''
        stats = None
        try:
            stats = self.metric.params.get('stats')
        except AttributeError:
            pass
        if stats:
            average = stats['average']
            std_dev = stats['std_dev']
            better_sign = stats['better_sign']
            return average, std_dev, better_sign
        else:
            return self.get_default_stats(source_data)

    def get_default_stats(self, source_data):
        '''
        Return population statistics

        Return is a 3-element tuple:
        - average - The average value for the population
        - standard deviation - The standard deviation for the population
        - better_sign - Positive if higher than average is good, negative if
          lower than average is good.
        '''
        raise NotImplementedError('get_default_stats not implemented')

    def calculate_by_boundary(self, boundary):
        '''Calculate by boundary, or use fake data if no data match'''
        calculation = super(
            PercentAlgorithm, self).calculate_by_boundary(boundary)
        if not calculation:
            fake = PlaceholderAlgorithm(self.node, self.metric, self.cache)
            calculation = fake.calculate_by_location(boundary.centroid.coords)
        return calculation

    def calculate_by_location(self, location):
        '''Calculate by location, or use fake data if no data match'''
        calculation = super(
            PercentAlgorithm, self).calculate_by_location(location)
        if not calculation:
            fake = PlaceholderAlgorithm(self.node, self.metric, self.cache)
            calculation = fake.calculate_by_location(location)
        return calculation


class CensusPercentAlgorithm(PercentAlgorithm):
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
        source_data = self.cache.get_data(Census, boundary)
        if not source_data:
            return None
        else:
            # Look for non-null, positive number in total fields
            total_fields, _ = self.get_fields()
            for field in total_fields:
                if getattr(source_data, field):
                    return source_data
            return None

    def local_percent(self, source_data):
        '''
        Calculate the local percentage for the source data
        '''
        total_fields, target_fields = self.get_fields()
        total = sum([getattr(source_data, f) for f in total_fields])
        target = sum([getattr(source_data, f) for f in target_fields])
        percent = float(target) / float(total)
        return percent

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


class FoodStampAlgorithm(CensusPercentAlgorithm):
    '''Score based on percentage of households on food stamps/assistance'''

    table = 'B19058'
    total_column_ids = (1,)
    target_column_ids = (2,)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.138
        std_dev = 0.106
        better_sign = -1
        return average, std_dev, better_sign


class PercentPovertyAlgorithm(CensusPercentAlgorithm):
    '''Score based on percentage of individuals below poverty level'''

    table = 'B17001'
    total_column_ids = (1,)
    target_column_ids = (2,)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.166
        std_dev = 0.118383
        better_sign = -1
        return average, std_dev, better_sign


def boundaries(point):
    raise Exception('Convert to new way')


def boundary_dict(boundary):
    raise Exception('Convert to new way')


class PercentUnemploymentAlgorithm(CensusPercentAlgorithm):
    '''
    Score based on employment status is unemployed for 16 and older
    '''

    table = 'B23001'
    total_column_ids = (1,)
    target_column_ids = (
        # Unemployed by age buckets
        8,   15,  22,  29,  36,  43,  50,  57,  64,  71,    # Male, 16 to 64
        76,  81,  86,                                       # Male, 65 and up
        94, 101, 108, 115, 122, 129, 136, 143, 150, 157,    # Female 16 to 64
        162, 167, 172)                                      # Female 65 and up

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.04193
        std_dev = 0.0266
        better_sign = -1
        return average, std_dev, better_sign


class PercentSingleParentAlgorithm(CensusPercentAlgorithm):
    '''
    Score based on # of children w/o two parents
    '''
    table = 'B09002'
    total_column_ids = (1,)
    target_column_ids = (8,)  # Count not in married-couple families

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.452998
        std_dev = 0.1657150
        better_sign = -1
        return average, std_dev, better_sign


class PercentIncomeHousingCostAlgorithm(CensusPercentAlgorithm):
    '''
    Score based on weighted percent requiring more than 35% of income

    Combines data from two tables:
    B25070: Gross Rent as a Percentage of Household Income
    B25091: Morgage Status by Selected Monthly Owner Costs as a Percentage of
            Household Income
    '''

    tables = {
        'B25070': {
            'total_column_ids': (1,),
            'target_column_ids': (8, 9, 10),
        },
        'B25091': {
            'total_column_ids': (1,),
            'target_column_ids': (9, 10, 11, 20, 21, 22),
        },
    }

    def get_fields(self):
        '''Get fields from both tables'''
        total_fields = []
        target_fields = []
        for table, columns in self.tables.items():
            pattern = table + '_{:03}E'
            total_fields.extend(
                [pattern.format(f) for f in columns['total_column_ids']])
            target_fields.extend(
                [pattern.format(f) for f in columns['target_column_ids']])
        return total_fields, target_fields

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.1544959
        std_dev = 0.0867039
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        '''Calculate a weighted percentage'''
        total_fields, _ = self.get_fields()
        total = sum([getattr(source_data, f) for f in total_fields])
        total_renter_gradual = (
            source_data.B25070_008E / float(4) +  # 35% - 39.9%
            source_data.B25070_009E / float(2) +  # 40% - 49.9%
            source_data.B25070_010E / float(1))   # 50% or more
        total_mortgaged_owner = (
            source_data.B25091_009E / float(4) +  # 35% - 39.9%
            source_data.B25091_010E / float(2) +  # 40% - 49.9%
            source_data.B25091_011E / float(1))   # 50% or more
        total_unmortgaged_owner = (
            source_data.B25091_020E / float(4) +  # 35% - 39.9%
            source_data.B25091_021E / float(2) +  # 40% - 49.9%
            source_data.B25091_022E / float(1))   # 50% or more
        weighted_percent_affordable = (
            total_renter_gradual + total_mortgaged_owner +
            total_unmortgaged_owner) / float(total)
        return weighted_percent_affordable


class PercentHighSchoolGraduatesAlgorithm(CensusPercentAlgorithm):
    '''
    Score based on population 25 or older with a high school diploma

    TODO: Switch to table B15003?
    '''
    table = 'B15002'
    total_column_ids = (1,)
    target_column_ids = (
        11, 12, 13, 14, 15, 16, 17, 18,  # Male, High School Grad or better
        28, 29, 30, 31, 32, 33, 34, 35)  # Female, High School Grad or better

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.861836
        std_dev = 0.096739
        better_sign = 1
        return average, std_dev, better_sign


class PercentDivorcedOrSeparatedAlgorithm(CensusPercentAlgorithm):
    '''
    Score based on population that is divorced or separated but not widowed
    '''
    table = 'B12001'
    total_column_ids = (1, )
    target_column_ids = (3, 9, 12, 18, 5, 14)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.264508
        std_dev = 0.139789
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        '''
        Calcuate the percent that were once married but aren't now
        '''
        total = source_data.B12001_001E
        never_married = source_data.B12001_003E + source_data.B12001_012E
        widowed = source_data.B12001_009E + source_data.B12001_018E
        married_and_present = source_data.B12001_005E + source_data.B12001_014E
        current_married_percent = (
            married_and_present / float(total - never_married - widowed))
        return 1.0 - current_married_percent


class PercentOvercrowdingAlgorithm(CensusPercentAlgorithm):
    '''Score based on weighted occupants per room'''
    table = 'B25014'
    total_column_ids = (1,)
    target_column_ids = (3, 4, 5, 6, 7, 9, 10, 11, 12, 13)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.040577
        std_dev = 0.014887
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        '''Return a weighted percentage of over-occupied residences'''
        total = source_data.B25014_001E
        # Get sum for owner-occupied and renter-occupied by occupants per room
        per_1_0 = source_data.B25014_004E + source_data.B25014_010E  # .5 - 1
        per_1_5 = source_data.B25014_005E + source_data.B25014_011E  # 1 - 1.5
        per_2_0 = source_data.B25014_006E + source_data.B25014_012E  # 1.5 - 2
        per_2_x = source_data.B25014_007E + source_data.B25014_013E  # > 2
        negative_weighted_sum = (
            per_1_0 / 8.0 + per_1_5 / 4.0 + per_2_0 / 2.0 + per_2_x)
        return negative_weighted_sum / float(total)


class PercentGeographicMobilityAlgorithm(CensusPercentAlgorithm):
    '''Score based on percent who did not live in the same house 1 year ago'''
    table = 'B07013'
    total_column_ids = (1,)
    target_column_ids = (4, )

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.168965
        std_dev = 0.09219
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        '''Calcuate the percent who moved in the last year'''
        total = source_data.B07013_001E
        same_house = source_data.B07013_004E  # Same house in the last year
        percent_same = same_house / float(total)
        return 1.0 - percent_same


class PercentCollegeGraduateAlgorithm(CensusPercentAlgorithm):
    '''Score based on percent who graduated college'''
    table = 'B15003'
    total_column_ids = (1,)
    target_column_ids = (21, 22, 23, 24, 25)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.301417
        std_dev = 0.153007
        better_sign = 1
        return average, std_dev, better_sign


class PercentBadCommuteTimesAlgorithm(CensusPercentAlgorithm):
    '''Score based on weighted percent of those with long commute times'''
    table = 'B08303'
    total_column_ids = (1, )
    target_column_ids = (8, 9, 10, 11, 12, 13)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.082964
        std_dev = 0.059340889
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        total = source_data.B08303_001E
        min_30 = source_data.B08303_008E  # 30 - 34 minutes
        min_35 = source_data.B08303_009E  # 35 - 39 minutes
        min_40 = source_data.B08303_010E  # 40 - 44 minutes
        min_45 = source_data.B08303_011E  # 45 - 59 minutes
        min_60 = source_data.B08303_012E  # 60 - 89 minutes
        min_90 = source_data.B08303_013E  # 90 or more minutes
        weighted = (
            (min_30 / 16.0) + (min_35 / 8.0) + (min_40 / 4.0) +
            (min_45 / 2.0) + min_60 + min_90)
        return weighted / float(total)


class PercentImproperKitchenFacilitiesAlgorithm(CensusPercentAlgorithm):
    '''Score based on if household lacks a complete kitchen'''
    table = 'B25052'
    total_column_ids = (1, )
    target_column_ids = (3, )

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.00976313
        std_dev = 0.01802429
        better_sign = -1
        return average, std_dev, better_sign


class PercentImproperPlumbingAlgorithm(CensusPercentAlgorithm):
    '''Score based on if household lacks complete plumbing'''
    table = 'B25048'
    total_column_ids = (1, )
    target_column_ids = (3, )

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.00572503
        std_dev = 0.0109313
        better_sign = -1
        return average, std_dev, better_sign


class PercentLowValueHousingAlgorithm(CensusPercentAlgorithm):
    '''Score based on value of owner-occupied housing units'''
    table = 'B25075'
    total_column_ids = (1, )
    target_column_ids = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    def get_default_stats(self, source_data):
        '''Stats for census tracts in Oklahoma'''
        average = 0.0575880
        std_dev = 0.057490381
        better_sign = -1
        return average, std_dev, better_sign

    def local_percent(self, source_data):
        total = source_data.B25075_001E
        k000 = source_data.B25075_002E / 1.0    # Less than $10k
        k010 = source_data.B25075_003E / 2.0    # $10k - $15k
        k015 = source_data.B25075_004E / 2.0    # $15k - $20k
        k020 = source_data.B25075_005E / 4.0    # $20k - $25k
        k025 = source_data.B25075_006E / 4.0    # $25k - $30k
        k030 = source_data.B25075_007E / 8.0    # $30k - $35k
        k035 = source_data.B25075_008E / 8.0    # $35k - $40k
        k040 = source_data.B25075_009E / 16.0   # $40k - $50k
        k050 = source_data.B25075_010E / 32.0   # $50k - $60k
        k060 = source_data.B25075_011E / 48.0   # $60k - $70k
        k070 = source_data.B25075_012E / 64.0   # $70k - $80k
        k080 = source_data.B25075_013E / 80.0   # $80k - $90k
        k090 = source_data.B25075_014E / 96.0   # $90k - $100k
        k100 = source_data.B25075_015E / 128.0  # $100k - $125k
        value = (
            k000 + k010 + k015 + k020 + k025 + k030 + k035 + k040 + k050 +
            k060 + k070 + k080 + k090 + k100)
        return value / float(total)


class DartmouthPercentAlgorithm(PercentAlgorithm):
    '''
    Algorithm for census-based calcuations of ratio vs. the state average
    '''
    # Default boundary set order
    boundary_set_slugs = ('counties', 'states')

    def source_data_for_boundary(self, boundary):
        '''Get data where the total population is not 0'''
        return self.cache.get_data(Dartmouth, boundary)


class PercentDischargeRateAlgorithm(DartmouthPercentAlgorithm):
    '''Score based on the Discharge Rate per 1000 Medicare Enrollees'''

    def local_percent(self, source_data):
        return float(source_data.discharge_rate_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.29159
        std_dev = 0.08387
        better_sign = -1
        return average, std_dev, better_sign


class ErsPercentAlgorithm(PercentAlgorithm):
    '''
    Algorithm for calculations of Ers data per county vs. the state average
    '''
    # Default boundary set order
    boundary_set_slugs = ('counties', 'states')

    def source_data_for_boundary(self, boundary):
        '''Get data for where the total population is not 0'''
        return self.cache.get_data(Ers, boundary)


class PercentAdultObesityAlgorithm(ErsPercentAlgorithm):
    '''Score based on percent of adults that are obese'''

    def local_percent(self, source_data):
        return float(source_data.per_adult_obesity)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.33388
        std_dev = 0.02308
        better_sign = -1
        return average, std_dev, better_sign


class PercentAdultDiabetesAlgorithm(ErsPercentAlgorithm):
    '''Score based on percent of adults that are Diabetic'''

    def local_percent(self, source_data):
        return float(source_data.per_adult_diabetes)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.1227
        std_dev = 0.01451
        better_sign = -1
        return average, std_dev, better_sign


class FitnessCentersPerCapitaAlgorithm(ErsPercentAlgorithm):
    '''Score based on fitness centers/recreation areas per 1000 people'''

    def local_percent(self, source_data):
        return float(source_data.rec_facilities_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.0000334103
        std_dev = 0.0000508600
        better_sign = 1
        return average, std_dev, better_sign


class FastFoodPerThousandAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the number of fast food restaurants per 1000 population
    '''

    def local_percent(self, source_data):
        return float(source_data.fast_food_rest_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.0004844545
        std_dev = 0.0002416161
        better_sign = -1
        return average, std_dev, better_sign


class FullRestPerThousandAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the number of full serivce restaurants per 1000 population
    '''

    def local_percent(self, source_data):
        return float(source_data.full_rest_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.0006372740
        std_dev = 0.0002420894
        better_sign = -1
        return average, std_dev, better_sign


class FarmersMarketsPerThousandAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the number of Farmer's Markets per 1000 population
    '''

    def local_percent(self, source_data):
        return float(source_data.farmers_markets_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.0000248259
        std_dev = 0.0000409239
        better_sign = 1
        return average, std_dev, better_sign


class PercentLowAccessToGroceriesAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the number of the population with low access to groceries
    '''

    def local_percent(self, source_data):
        return float(source_data.per_low_access_to_groceries)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.278403948
        std_dev = 0.187626943
        better_sign = -1
        return average, std_dev, better_sign


class GroceryStoresPerThousandAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the number of Grocery Stores per Thousand Population
    '''

    def local_percent(self, source_data):
        return float(source_data.grocery_stores_per_capita)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.0002111467
        std_dev = 0.0001415997
        better_sign = 1
        return average, std_dev, better_sign


class PercentFreeLunchAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the percent of students that qualify for a free lunch
    '''

    def local_percent(self, source_data):
        return float(source_data.per_students_for_free_lunch)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.53579519
        std_dev = 0.095828258
        better_sign = -1
        return average, std_dev, better_sign


class PercentReducedLunchAlgorithm(ErsPercentAlgorithm):
    '''
    Score based on the percent of students that qualify for a free lunch
    '''

    def local_percent(self, source_data):
        return float(source_data.per_students_for_reduced_lunch)

    def get_default_stats(self, source_data):
        '''Stats for counties in Oklahoma'''
        average = 0.53579519
        std_dev = 0.095828258
        better_sign = -1
        return average, std_dev, better_sign
