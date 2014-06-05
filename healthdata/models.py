from boundaryservice.models import Boundary
from django.db import models
from jsonfield import JSONField
from mptt.models import MPTTModel, TreeForeignKey
from south.modelsinspector import add_introspection_rules

import algorithms


add_introspection_rules(
    [], ['^django\.contrib\.gis\.db\.models\.fields\.MultiPolygonField'])
add_introspection_rules(
    [], ['^django\.contrib\.gis\.db\.models\.fields\.PointField'])


class ProtoHealth(models.Model):
    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    fips = models.CharField('FIPS', max_length=8)
    population = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    perc_poor = models.FloatField('% Fair/Poor', blank=True, null=True)
    perc_lbw = models.FloatField('% LBW', blank=True, null=True)
    perc_smokers = models.FloatField('% Smokers', blank=True, null=True)
    perc_obese = models.FloatField('% Obese', blank=True, null=True)
    std_rate = models.FloatField(
        'STD Rates per 100,000', blank=True, null=True)
    teen_birth_rate = models.FloatField(blank=True, null=True)
    mammography_rate = models.FloatField(blank=True, null=True)
    perc_unemployed = models.FloatField('% Unemployed', blank=True, null=True)
    perc_children_poverty = models.FloatField(
        '% Children in Poverty', blank=True, null=True)
    violent_crime = models.FloatField(
        'Violent Crime Rate', blank=True, null=True)
    ozone_days = models.IntegerField(blank=True, null=True)
    perc_limited_food = models.FloatField(
        '% Limited Access Food', blank=True, null=True)
    perc_fast_food = models.FloatField('% Fast Foods', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.boundary


class ScoreMetric(models.Model):
    '''A metric that has a score for a given location'''

    PLACEHOLDER_ALGORITHM = 0
    FOOD_STAMP_ALGORITHM = 1
    PERCENT_POVERTY_ALGORITHM = 2
    PERCENT_UNEMPLOYMENT_ALGORITHM = 3
    PERCENT_SINGLE_PARENT_ALGORITHM = 4
    PERCENT_INCOME_HOUSING_COST_ALGORITHM = 5
    PERCENT_HIGH_SCHOOL_GRADUATES_ALGORITHM = 6
    PERCENT_DIVORCED_ALGORITHM = 7
    PERCENT_OVERCROWDING_ALGORITHM = 8
    PERCENT_GEOGRAPHIC_MOBILITY_ALGORITHM = 9
    PERCENT_COLLEGE_GRADUATE_ALGORITHM = 10
    PERCENT_BAD_COMMUTE_TIMES_ALGORITHM = 11
    PERCENT_IMPROPER_KITCHEN_FACILITIES_ALGORITHM = 12
    PERCENT_IMPROPER_PLUMBING_ALGORITHM = 13
    PERCENT_LOW_VALUE_HOUSING_ALGORITHM = 14
    algorithm_choices = (
        (PLACEHOLDER_ALGORITHM, 'PlaceholderAlgorithm',
            'Placeholder Algorithm'),
        (FOOD_STAMP_ALGORITHM, 'FoodStampAlgorithm', 'Food Stamp Algorithm'),
        (PERCENT_POVERTY_ALGORITHM, 'PercentPovertyAlgorithm',
         'Percent Poverty Algorithm'),
        (PERCENT_UNEMPLOYMENT_ALGORITHM, 'PercentUnemploymentAlgorithm',
         'Percent Unemployment Algorithm'),
        (PERCENT_SINGLE_PARENT_ALGORITHM, 'PercentSingleParentAlgorithm',
         'Percent Single Parent Algorithm'),
        (PERCENT_INCOME_HOUSING_COST_ALGORITHM,
         'PercentIncomeHousingCostAlgorithm',
         'Percent Income Housing Cost Algorithm'),
        (PERCENT_HIGH_SCHOOL_GRADUATES_ALGORITHM,
         'PercentHighSchoolGraduatesAlgorithm',
         'Percent High School Graduates Algorithm'),
        (PERCENT_DIVORCED_ALGORITHM,
         'PercentDivorcedOrSeparatedAlgorithm',
         'Percent Divorced or Separated Algorithm'),
        (PERCENT_OVERCROWDING_ALGORITHM,
         'PercentOvercrowdingAlgorithm',
         'Percent Overcrowding Algorithm'),
        (PERCENT_GEOGRAPHIC_MOBILITY_ALGORITHM,
         'PercentGeographicMobilityAlgorithm',
         'Percent Geographic Mobility Algorithm'),
        (PERCENT_COLLEGE_GRADUATE_ALGORITHM,
         'PercentCollegeGraduateAlgorithm',
         'Percent College Graduate Algorithm'),
        (PERCENT_BAD_COMMUTE_TIMES_ALGORITHM,
         'PercentBadCommuteTimesAlgorithm',
         'Percent Bad Commute Times Algorithm'),
        (PERCENT_IMPROPER_KITCHEN_FACILITIES_ALGORITHM,
         'PercentImproperKitchenFacilitiesAlgorithm',
         'Percent Improper Kitchen Facilities'),
        (PERCENT_IMPROPER_PLUMBING_ALGORITHM,
         'PercentImproperPlumbingAlgorithm',
         'Percent Improper Plumbing Algorithm'),
        (PERCENT_LOW_VALUE_HOUSING_ALGORITHM,
         'PercentLowValueHousingAlgorithm',
         'Percent Low Value Housing Algorithm'),
    )
    algorithm_class_name = dict([(a[0], a[1]) for a in algorithm_choices])

    name = models.CharField(
        max_length=50, help_text='Short human-readable name')
    description = models.CharField(
        max_length=255, default="This is a description",
        help_text='Human-readable description')
    algorithm = models.IntegerField(
        choices=[(a[0], a[2]) for a in algorithm_choices],
        default=PLACEHOLDER_ALGORITHM,
        help_text='Algorithm used to calculate score')
    params = JSONField(
        default='', null=True, blank=True,
        help_text="Extra parameters for algorithm")

    def __str__(self):
        return self.name

    def get_algorithm(self, node):
        klass = getattr(algorithms, self.algorithm_class_name[self.algorithm])
        algorithm = klass(node, self)
        return algorithm

    def score_by_boundary(self, node, boundary):
        return self.get_algorithm(node).calculate_by_boundary(boundary)

    def score_by_location(self, node, location):
        return self.get_algorithm(node).calculate_by_location(location)


class ScoreNode(MPTTModel):
    '''A node in the tree of scored metrics'''

    label = models.CharField(
        max_length=255, help_text='Human-readable name')
    slug = models.CharField(
        max_length=50, help_text='Short slugified name for assets')
    rel_order = models.IntegerField(
        default=100, help_text="Relative ordering of sibling nodes")
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')
    weight = models.IntegerField(
        default=1, help_text="Relative weight of this node to siblings")
    metric = models.ForeignKey(ScoreMetric, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['rel_order', 'slug']

    def __str__(self):
        return self.label

    def score_by_boundary(self, boundary):
        if self.metric:
            return self.metric.score_by_boundary(self, boundary)
        else:
            return None

    def score_by_location(self, location):
        if self.metric:
            return self.metric.score_by_location(self, location)
        else:
            return None
