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
    fast_food_rest_per_thousand = models.FloatField(
        blank=True, null=True,
        help_text='Fast Food Restaurants per 1000 Population')
    full_rest_per_thousand = models.FloatField(
        blank=True, null=True,
        help_text='Full Service Restaurants per 1000 Population')
    farmers_markets_per_thousand = models.FloatField(
        blank=True, null=True,
        help_text='Farmers Markets per 1000 Population')
    percent_low_access_to_groceries = models.FloatField(
        blank=True, null=True,
        help_text='Population with a Low Access to Grocery Stores')
    grocery_stores_per_thousand = models.FloatField(
        blank=True, null=True,
        help_text='Grocery Stores per 1000 Population')
    percent_students_for_free_lunch = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Students Eligible for a Free Lunch')
    percent_students_for_reduced_lunch = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Students Eligible for a Reduced Price Lunch')



