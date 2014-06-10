from django.db import models
from boundaryservice.models import Boundary


class Dartmouth(models.Model):
    '''Data from Dartmouth Atlas of Health Care'''

    class Meta:
        verbose_name_plural = "dartmouth"
        app_label = "data"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    discharge_rate = models.FloatField(
        blank=True, null=True,
        help_text='Discharge Rate Per 1000 Medicare Enrollees')
