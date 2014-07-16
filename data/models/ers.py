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
    per_adult_diabetes = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Adults with Diabetes')
    per_adult_obesity = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Adults that are Obese')
    rec_facilities_per_capita = models.FloatField(
        blank=True, null=True,
        help_text='Recreational Facilities per Resident')
    fast_food_rest_per_capita = models.FloatField(
        blank=True, null=True,
        help_text='Fast Food Restaurants per Resident')
    full_rest_per_capita = models.FloatField(
        blank=True, null=True,
        help_text='Full Service Restaurants per Resident')
    farmers_markets_per_capita = models.FloatField(
        blank=True, null=True,
        help_text='Farmers Markets per Resident')
    per_low_access_to_groceries = models.FloatField(
        blank=True, null=True,
        help_text='Percent of the Population with Low Access to Groceries')
    grocery_stores_per_capita = models.FloatField(
        blank=True, null=True,
        help_text='Grocery Stores per Resident')
    per_students_for_free_lunch = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Students Eligible for a Free Lunch')
    per_students_for_reduced_lunch = models.FloatField(
        blank=True, null=True,
        help_text='Percent of Students Eligible for a Reduced Price Lunch')
