from boundaryservice.models import Boundary, BoundarySet
from django.db import models
from django.contrib.contenttypes.models import ContentType
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

    FAKE_ALGORITHM = 0
    FOOD_STAMP_ALGORITHM = 1
    PERCENT_POVERTY_ALGORITHM = 2
    algorithm_choices = (
        (FAKE_ALGORITHM, 'FakeAlgorithm', 'Fake Algorithm'),
        (FOOD_STAMP_ALGORITHM, 'FoodStampAlgorithm', 'Food Stamp Algorithm'),
        (PERCENT_POVERTY_ALGORITHM, 'PercentPovertyAlgorithm', 'Percent Poverty Algorithm'),
    )
    algorithm_class_name = dict([(a[0], a[1]) for a in algorithm_choices])

    name = models.CharField(
        max_length=50, help_text='Short human-readable name')
    description = models.CharField(
        max_length=255, default="This is a description",
        help_text='Human-readable description')
    data_source = models.ForeignKey(
        ContentType, null=True, blank=True,
        help_text='Model that Holds the Source Data')
    boundary_set = models.ForeignKey(
        BoundarySet, null=True, blank=True,
        help_text='Related Boundary Set with Data')
    data_property = models.CharField(
        max_length=50, null=True, blank=True,
        help_text='Data property used for source data')
    algorithm = models.IntegerField(
        choices=[(a[0], a[2]) for a in algorithm_choices],
        default=FAKE_ALGORITHM,
        help_text='Algorithm used to calculate score')
    params = JSONField(
        default='', null=True, blank=True,
        help_text="Extra parameters for algorithm")

    def __str__(self):
        return self.name

    def get_algorithm(self):
        klass = getattr(algorithms, self.algorithm_class_name[self.algorithm])
        algorithm = klass(self)
        return algorithm


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
