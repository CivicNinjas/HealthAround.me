from boundaryservice.models import Boundary
from django.db import models
from south.modelsinspector import add_introspection_rules



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
