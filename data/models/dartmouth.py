from django.db import models
from boundaryservice.models import Boundary


class Dartmouth(models.Model):
    '''Data from Dartmouth Atlas of Health Care'''

    class Meta:
        verbose_name_plural = "dartmouth"
        app_label = "data"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    discharge_rate = models.DecimalField(
        max_digits=5, decimal_places=1,
        blank=True, null=True,
        help_text='Discharge Rate Per 1000 Medicare Enrollees')
