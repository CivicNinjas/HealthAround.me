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
