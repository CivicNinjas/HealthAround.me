from django.db import models
from boundaryservice.models import Boundary


class Ers(models.Model):
    '''Data from the USDA Economic Research Survey'''

    class Meta:
        verbose_name_plural = "ers"
        app_label = "data"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    adult_diabetes = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Adults with Diabetes')
    adult_obesity = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Adults that are Obese')
    childhood_obesity = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Children that are Obese')
    rec_facilities_per_thousand = models.FloatField(
        blank=True, null=True,
        help_text='Recreational Facilities in County per 1,000 Residents')


