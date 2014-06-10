from django.db import models
from boundaryservice.models import Boundary


class Census(models.Model):
    '''Selected items from U.S. Census 5-Year Summary for Boundary'''

    class Meta:
        verbose_name_plural = "census"
        app_label = "data"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    logical_num = models.IntegerField(help_text='Logical record number')

    # B07013 - Geographical Mobility In the Past Year by Tenure For
    #          Current Residence In the United States
    B07013_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Geographical Mobility In the Past Year by Tenure For Current'
            ' Residence In the United States: Total:'))
    B07013_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')
    B07013_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Same house 1 year ago:')
    B07013_005E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_006E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')
    B07013_007E = models.IntegerField(
        blank=True, null=True,
        help_text='Moved within same county:')
    B07013_008E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_009E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')
    B07013_010E = models.IntegerField(
        blank=True, null=True,
        help_text='Moved from different county within same state:')
    B07013_011E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_012E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')
    B07013_013E = models.IntegerField(
        blank=True, null=True,
        help_text='Moved from different state:')
    B07013_014E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_015E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')
    B07013_016E = models.IntegerField(
        blank=True, null=True,
        help_text='Moved from abroad:')
    B07013_017E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in owner-occupied housing units')
    B07013_018E = models.IntegerField(
        blank=True, null=True,
        help_text='Householder lived in renter-occupied housing units')

    # B08303 - Travel Time to Work
    B08303_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Travel Time to Work: Total:')
    B08303_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Less than 5 minutes')
    B08303_003E = models.IntegerField(
        blank=True, null=True,
        help_text='5 to 9 minutes')
    B08303_004E = models.IntegerField(
        blank=True, null=True,
        help_text='10 to 14 minutes')
    B08303_005E = models.IntegerField(
        blank=True, null=True,
        help_text='15 to 19 minutes')
    B08303_006E = models.IntegerField(
        blank=True, null=True,
        help_text='20 to 24 minutes')
    B08303_007E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 29 minutes')
    B08303_008E = models.IntegerField(
        blank=True, null=True,
        help_text='30 to 34 minutes')
    B08303_009E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 39 minutes')
    B08303_010E = models.IntegerField(
        blank=True, null=True,
        help_text='40 to 44 minutes')
    B08303_011E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 59 minutes')
    B08303_012E = models.IntegerField(
        blank=True, null=True,
        help_text='60 to 89 minutes')
    B08303_013E = models.IntegerField(
        blank=True, null=True,
        help_text='90 or more minutes')

    # B09002 - Own Children Under 18 Years by Family Type And Age
    B09002_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Own Children Under 18 Years by Family Type And Age: Total:')
    B09002_002E = models.IntegerField(
        blank=True, null=True,
        help_text='In married-couple families:')
    B09002_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 3 years')
    B09002_004E = models.IntegerField(
        blank=True, null=True,
        help_text='3 and 4 years')
    B09002_005E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B09002_006E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B09002_007E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 17 years')
    B09002_008E = models.IntegerField(
        blank=True, null=True,
        help_text='In other families:')
    B09002_009E = models.IntegerField(
        blank=True, null=True,
        help_text='Male householder, no wife present:')
    B09002_010E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 3 years')
    B09002_011E = models.IntegerField(
        blank=True, null=True,
        help_text='3 and 4 years')
    B09002_012E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B09002_013E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B09002_014E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 17 years')
    B09002_015E = models.IntegerField(
        blank=True, null=True,
        help_text='Female householder, no husband present:')
    B09002_016E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 3 years')
    B09002_017E = models.IntegerField(
        blank=True, null=True,
        help_text='3 and 4 years')
    B09002_018E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B09002_019E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B09002_020E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 17 years')

    # B12001 - Sex by Marital Status For the Population 15 Years And Over
    B12001_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Sex by Marital Status For the Population 15 Years And Over:'
            ' Total:'))
    B12001_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B12001_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Never married')
    B12001_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Now married:')
    B12001_005E = models.IntegerField(
        blank=True, null=True,
        help_text='Married, spouse present')
    B12001_006E = models.IntegerField(
        blank=True, null=True,
        help_text='Married, spouse absent:')
    B12001_007E = models.IntegerField(
        blank=True, null=True,
        help_text='Separated')
    B12001_008E = models.IntegerField(
        blank=True, null=True,
        help_text='Other')
    B12001_009E = models.IntegerField(
        blank=True, null=True,
        help_text='Widowed')
    B12001_010E = models.IntegerField(
        blank=True, null=True,
        help_text='Divorced')
    B12001_011E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B12001_012E = models.IntegerField(
        blank=True, null=True,
        help_text='Never married')
    B12001_013E = models.IntegerField(
        blank=True, null=True,
        help_text='Now married:')
    B12001_014E = models.IntegerField(
        blank=True, null=True,
        help_text='Married, spouse present')
    B12001_015E = models.IntegerField(
        blank=True, null=True,
        help_text='Married, spouse absent:')
    B12001_016E = models.IntegerField(
        blank=True, null=True,
        help_text='Separated')
    B12001_017E = models.IntegerField(
        blank=True, null=True,
        help_text='Other')
    B12001_018E = models.IntegerField(
        blank=True, null=True,
        help_text='Widowed')
    B12001_019E = models.IntegerField(
        blank=True, null=True,
        help_text='Divorced')

    # B12503 - Divorces In the Last Year by Sex by Marital Status For
    #          the Population 15 Years And Over
    B12503_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Divorces In the Last Year by Sex by Marital Status For the'
            ' Population 15 Years And Over: Total:'))
    B12503_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B12503_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Never married')
    B12503_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Ever married:')
    B12503_005E = models.IntegerField(
        blank=True, null=True,
        help_text='Divorced last year')
    B12503_006E = models.IntegerField(
        blank=True, null=True,
        help_text='Not divorced last year')
    B12503_007E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B12503_008E = models.IntegerField(
        blank=True, null=True,
        help_text='Never married')
    B12503_009E = models.IntegerField(
        blank=True, null=True,
        help_text='Ever married:')
    B12503_010E = models.IntegerField(
        blank=True, null=True,
        help_text='Divorced last year')
    B12503_011E = models.IntegerField(
        blank=True, null=True,
        help_text='Not divorced last year')

    # B15002 - Sex by Educational Attainment For the Population 25
    #          Years And Over
    B15002_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Sex by Educational Attainment For the Population 25 Years And'
            ' Over: Total:'))
    B15002_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B15002_003E = models.IntegerField(
        blank=True, null=True,
        help_text='No schooling completed')
    B15002_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Nursery to 4th grade')
    B15002_005E = models.IntegerField(
        blank=True, null=True,
        help_text='5th and 6th grade')
    B15002_006E = models.IntegerField(
        blank=True, null=True,
        help_text='7th and 8th grade')
    B15002_007E = models.IntegerField(
        blank=True, null=True,
        help_text='9th grade')
    B15002_008E = models.IntegerField(
        blank=True, null=True,
        help_text='10th grade')
    B15002_009E = models.IntegerField(
        blank=True, null=True,
        help_text='11th grade')
    B15002_010E = models.IntegerField(
        blank=True, null=True,
        help_text='12th grade, no diploma')
    B15002_011E = models.IntegerField(
        blank=True, null=True,
        help_text='High school graduate, GED, or alternative')
    B15002_012E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, less than 1 year')
    B15002_013E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, 1 or more years, no degree')
    B15002_014E = models.IntegerField(
        blank=True, null=True,
        help_text='Associate\'s degree')
    B15002_015E = models.IntegerField(
        blank=True, null=True,
        help_text='Bachelor\'s degree')
    B15002_016E = models.IntegerField(
        blank=True, null=True,
        help_text='Master\'s degree')
    B15002_017E = models.IntegerField(
        blank=True, null=True,
        help_text='Professional school degree')
    B15002_018E = models.IntegerField(
        blank=True, null=True,
        help_text='Doctorate degree')
    B15002_019E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B15002_020E = models.IntegerField(
        blank=True, null=True,
        help_text='No schooling completed')
    B15002_021E = models.IntegerField(
        blank=True, null=True,
        help_text='Nursery to 4th grade')
    B15002_022E = models.IntegerField(
        blank=True, null=True,
        help_text='5th and 6th grade')
    B15002_023E = models.IntegerField(
        blank=True, null=True,
        help_text='7th and 8th grade')
    B15002_024E = models.IntegerField(
        blank=True, null=True,
        help_text='9th grade')
    B15002_025E = models.IntegerField(
        blank=True, null=True,
        help_text='10th grade')
    B15002_026E = models.IntegerField(
        blank=True, null=True,
        help_text='11th grade')
    B15002_027E = models.IntegerField(
        blank=True, null=True,
        help_text='12th grade, no diploma')
    B15002_028E = models.IntegerField(
        blank=True, null=True,
        help_text='High school graduate, GED, or alternative')
    B15002_029E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, less than 1 year')
    B15002_030E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, 1 or more years, no degree')
    B15002_031E = models.IntegerField(
        blank=True, null=True,
        help_text='Associate\'s degree')
    B15002_032E = models.IntegerField(
        blank=True, null=True,
        help_text='Bachelor\'s degree')
    B15002_033E = models.IntegerField(
        blank=True, null=True,
        help_text='Master\'s degree')
    B15002_034E = models.IntegerField(
        blank=True, null=True,
        help_text='Professional school degree')
    B15002_035E = models.IntegerField(
        blank=True, null=True,
        help_text='Doctorate degree')

    # B15003 - Educational Attainment For the Population 25 Years And Over
    B15003_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Educational Attainment For the Population 25 Years And Over:'
            ' Total:'))
    B15003_002E = models.IntegerField(
        blank=True, null=True,
        help_text='No schooling completed')
    B15003_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Nursery school')
    B15003_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Kindergarten')
    B15003_005E = models.IntegerField(
        blank=True, null=True,
        help_text='1st grade')
    B15003_006E = models.IntegerField(
        blank=True, null=True,
        help_text='2nd grade')
    B15003_007E = models.IntegerField(
        blank=True, null=True,
        help_text='3rd grade')
    B15003_008E = models.IntegerField(
        blank=True, null=True,
        help_text='4th grade')
    B15003_009E = models.IntegerField(
        blank=True, null=True,
        help_text='5th grade')
    B15003_010E = models.IntegerField(
        blank=True, null=True,
        help_text='6th grade')
    B15003_011E = models.IntegerField(
        blank=True, null=True,
        help_text='7th grade')
    B15003_012E = models.IntegerField(
        blank=True, null=True,
        help_text='8th grade')
    B15003_013E = models.IntegerField(
        blank=True, null=True,
        help_text='9th grade')
    B15003_014E = models.IntegerField(
        blank=True, null=True,
        help_text='10th grade')
    B15003_015E = models.IntegerField(
        blank=True, null=True,
        help_text='11th grade')
    B15003_016E = models.IntegerField(
        blank=True, null=True,
        help_text='12th grade, no diploma')
    B15003_017E = models.IntegerField(
        blank=True, null=True,
        help_text='Regular high school diploma')
    B15003_018E = models.IntegerField(
        blank=True, null=True,
        help_text='GED or alternative credential')
    B15003_019E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, less than 1 year')
    B15003_020E = models.IntegerField(
        blank=True, null=True,
        help_text='Some college, 1 or more years, no degree')
    B15003_021E = models.IntegerField(
        blank=True, null=True,
        help_text='Associate\'s degree')
    B15003_022E = models.IntegerField(
        blank=True, null=True,
        help_text='Bachelor\'s degree')
    B15003_023E = models.IntegerField(
        blank=True, null=True,
        help_text='Master\'s degree')
    B15003_024E = models.IntegerField(
        blank=True, null=True,
        help_text='Professional school degree')
    B15003_025E = models.IntegerField(
        blank=True, null=True,
        help_text='Doctorate degree')

    # B17001 - Poverty Status In the Past 12 Months by Sex by Age
    B17001_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Poverty Status In the Past 12 Months by Sex by Age: Total:')
    B17001_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Income in the past 12 months below poverty level:')
    B17001_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B17001_004E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 5 years')
    B17001_005E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B17001_006E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B17001_007E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 14 years')
    B17001_008E = models.IntegerField(
        blank=True, null=True,
        help_text='15 years')
    B17001_009E = models.IntegerField(
        blank=True, null=True,
        help_text='16 and 17 years')
    B17001_010E = models.IntegerField(
        blank=True, null=True,
        help_text='18 to 24 years')
    B17001_011E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 34 years')
    B17001_012E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years')
    B17001_013E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years')
    B17001_014E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 64 years')
    B17001_015E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 74 years')
    B17001_016E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over')
    B17001_017E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B17001_018E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 5 years')
    B17001_019E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B17001_020E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B17001_021E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 14 years')
    B17001_022E = models.IntegerField(
        blank=True, null=True,
        help_text='15 years')
    B17001_023E = models.IntegerField(
        blank=True, null=True,
        help_text='16 and 17 years')
    B17001_024E = models.IntegerField(
        blank=True, null=True,
        help_text='18 to 24 years')
    B17001_025E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 34 years')
    B17001_026E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years')
    B17001_027E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years')
    B17001_028E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 64 years')
    B17001_029E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 74 years')
    B17001_030E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over')
    B17001_031E = models.IntegerField(
        blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level:')
    B17001_032E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B17001_033E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 5 years')
    B17001_034E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B17001_035E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B17001_036E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 14 years')
    B17001_037E = models.IntegerField(
        blank=True, null=True,
        help_text='15 years')
    B17001_038E = models.IntegerField(
        blank=True, null=True,
        help_text='16 and 17 years')
    B17001_039E = models.IntegerField(
        blank=True, null=True,
        help_text='18 to 24 years')
    B17001_040E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 34 years')
    B17001_041E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years')
    B17001_042E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years')
    B17001_043E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 64 years')
    B17001_044E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 74 years')
    B17001_045E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over')
    B17001_046E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B17001_047E = models.IntegerField(
        blank=True, null=True,
        help_text='Under 5 years')
    B17001_048E = models.IntegerField(
        blank=True, null=True,
        help_text='5 years')
    B17001_049E = models.IntegerField(
        blank=True, null=True,
        help_text='6 to 11 years')
    B17001_050E = models.IntegerField(
        blank=True, null=True,
        help_text='12 to 14 years')
    B17001_051E = models.IntegerField(
        blank=True, null=True,
        help_text='15 years')
    B17001_052E = models.IntegerField(
        blank=True, null=True,
        help_text='16 and 17 years')
    B17001_053E = models.IntegerField(
        blank=True, null=True,
        help_text='18 to 24 years')
    B17001_054E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 34 years')
    B17001_055E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years')
    B17001_056E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years')
    B17001_057E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 64 years')
    B17001_058E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 74 years')
    B17001_059E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over')

    # B19058 - Public Assistance Income Or Food Stamps/Snap In the Past
    #          12 Months For Households
    B19058_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Public Assistance Income Or Food Stamps/Snap In the Past 12'
            ' Months For Households: Total:'))
    B19058_002E = models.IntegerField(
        blank=True, null=True,
        help_text='With cash public assistance or Food Stamps/SNAP')
    B19058_003E = models.IntegerField(
        blank=True, null=True,
        help_text='No cash public assistance or Food Stamps/SNAP')

    # B23001 - Sex by Age by Employment Status For the Population 16
    #          Years And Over
    B23001_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Sex by Age by Employment Status For the Population 16 Years And'
            ' Over: Total:'))
    B23001_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Male:')
    B23001_003E = models.IntegerField(
        blank=True, null=True,
        help_text='16 to 19 years:')
    B23001_004E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_005E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_006E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_007E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_008E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_009E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_010E = models.IntegerField(
        blank=True, null=True,
        help_text='20 and 21 years:')
    B23001_011E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_012E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_013E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_014E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_015E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_016E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_017E = models.IntegerField(
        blank=True, null=True,
        help_text='22 to 24 years:')
    B23001_018E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_019E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_020E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_021E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_022E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_023E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_024E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 29 years:')
    B23001_025E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_026E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_027E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_028E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_029E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_030E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_031E = models.IntegerField(
        blank=True, null=True,
        help_text='30 to 34 years:')
    B23001_032E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_033E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_034E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_035E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_036E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_037E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_038E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years:')
    B23001_039E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_040E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_041E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_042E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_043E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_044E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_045E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years:')
    B23001_046E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_047E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_048E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_049E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_050E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_051E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_052E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 59 years:')
    B23001_053E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_054E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_055E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_056E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_057E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_058E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_059E = models.IntegerField(
        blank=True, null=True,
        help_text='60 and 61 years:')
    B23001_060E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_061E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_062E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_063E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_064E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_065E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_066E = models.IntegerField(
        blank=True, null=True,
        help_text='62 to 64 years:')
    B23001_067E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_068E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_069E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_070E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_071E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_072E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_073E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 69 years:')
    B23001_074E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_075E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_076E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_077E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_078E = models.IntegerField(
        blank=True, null=True,
        help_text='70 to 74 years:')
    B23001_079E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_080E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_081E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_082E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_083E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over:')
    B23001_084E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_085E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_086E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_087E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_088E = models.IntegerField(
        blank=True, null=True,
        help_text='Female:')
    B23001_089E = models.IntegerField(
        blank=True, null=True,
        help_text='16 to 19 years:')
    B23001_090E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_091E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_092E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_093E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_094E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_095E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_096E = models.IntegerField(
        blank=True, null=True,
        help_text='20 and 21 years:')
    B23001_097E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_098E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_099E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_100E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_101E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_102E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_103E = models.IntegerField(
        blank=True, null=True,
        help_text='22 to 24 years:')
    B23001_104E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_105E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_106E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_107E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_108E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_109E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_110E = models.IntegerField(
        blank=True, null=True,
        help_text='25 to 29 years:')
    B23001_111E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_112E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_113E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_114E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_115E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_116E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_117E = models.IntegerField(
        blank=True, null=True,
        help_text='30 to 34 years:')
    B23001_118E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_119E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_120E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_121E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_122E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_123E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_124E = models.IntegerField(
        blank=True, null=True,
        help_text='35 to 44 years:')
    B23001_125E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_126E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_127E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_128E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_129E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_130E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_131E = models.IntegerField(
        blank=True, null=True,
        help_text='45 to 54 years:')
    B23001_132E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_133E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_134E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_135E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_136E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_137E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_138E = models.IntegerField(
        blank=True, null=True,
        help_text='55 to 59 years:')
    B23001_139E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_140E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_141E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_142E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_143E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_144E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_145E = models.IntegerField(
        blank=True, null=True,
        help_text='60 and 61 years:')
    B23001_146E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_147E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_148E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_149E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_150E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_151E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_152E = models.IntegerField(
        blank=True, null=True,
        help_text='62 to 64 years:')
    B23001_153E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_154E = models.IntegerField(
        blank=True, null=True,
        help_text='In Armed Forces')
    B23001_155E = models.IntegerField(
        blank=True, null=True,
        help_text='Civilian:')
    B23001_156E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_157E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_158E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_159E = models.IntegerField(
        blank=True, null=True,
        help_text='65 to 69 years:')
    B23001_160E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_161E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_162E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_163E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_164E = models.IntegerField(
        blank=True, null=True,
        help_text='70 to 74 years:')
    B23001_165E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_166E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_167E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_168E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')
    B23001_169E = models.IntegerField(
        blank=True, null=True,
        help_text='75 years and over:')
    B23001_170E = models.IntegerField(
        blank=True, null=True,
        help_text='In labor force:')
    B23001_171E = models.IntegerField(
        blank=True, null=True,
        help_text='Employed')
    B23001_172E = models.IntegerField(
        blank=True, null=True,
        help_text='Unemployed')
    B23001_173E = models.IntegerField(
        blank=True, null=True,
        help_text='Not in labor force')

    # B25014 - Tenure by Occupants Per Room
    B25014_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Tenure by Occupants Per Room: Total:')
    B25014_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Owner occupied:')
    B25014_003E = models.IntegerField(
        blank=True, null=True,
        help_text='0.50 or less occupants per room')
    B25014_004E = models.IntegerField(
        blank=True, null=True,
        help_text='0.51 to 1.00 occupants per room')
    B25014_005E = models.IntegerField(
        blank=True, null=True,
        help_text='1.01 to 1.50 occupants per room')
    B25014_006E = models.IntegerField(
        blank=True, null=True,
        help_text='1.51 to 2.00 occupants per room')
    B25014_007E = models.IntegerField(
        blank=True, null=True,
        help_text='2.01 or more occupants per room')
    B25014_008E = models.IntegerField(
        blank=True, null=True,
        help_text='Renter occupied:')
    B25014_009E = models.IntegerField(
        blank=True, null=True,
        help_text='0.50 or less occupants per room')
    B25014_010E = models.IntegerField(
        blank=True, null=True,
        help_text='0.51 to 1.00 occupants per room')
    B25014_011E = models.IntegerField(
        blank=True, null=True,
        help_text='1.01 to 1.50 occupants per room')
    B25014_012E = models.IntegerField(
        blank=True, null=True,
        help_text='1.51 to 2.00 occupants per room')
    B25014_013E = models.IntegerField(
        blank=True, null=True,
        help_text='2.01 or more occupants per room')

    # B25048 - Plumbing Facilities For Occupied Housing Units
    B25048_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Plumbing Facilities For Occupied Housing Units: Total:')
    B25048_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Complete plumbing facilities')
    B25048_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Lacking complete plumbing facilities')

    # B25052 - Kitchen Facilities For Occupied Housing Units
    B25052_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Kitchen Facilities For Occupied Housing Units: Total:')
    B25052_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Complete kitchen facilities')
    B25052_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Lacking complete kitchen facilities')

    # B25070 - Gross Rent As a Percentage of Household Income In the
    #          Past 12 Months
    B25070_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Gross Rent As a Percentage of Household Income In the Past 12'
            ' Months: Total:'))
    B25070_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Less than 10.0 percent')
    B25070_003E = models.IntegerField(
        blank=True, null=True,
        help_text='10.0 to 14.9 percent')
    B25070_004E = models.IntegerField(
        blank=True, null=True,
        help_text='15.0 to 19.9 percent')
    B25070_005E = models.IntegerField(
        blank=True, null=True,
        help_text='20.0 to 24.9 percent')
    B25070_006E = models.IntegerField(
        blank=True, null=True,
        help_text='25.0 to 29.9 percent')
    B25070_007E = models.IntegerField(
        blank=True, null=True,
        help_text='30.0 to 34.9 percent')
    B25070_008E = models.IntegerField(
        blank=True, null=True,
        help_text='35.0 to 39.9 percent')
    B25070_009E = models.IntegerField(
        blank=True, null=True,
        help_text='40.0 to 49.9 percent')
    B25070_010E = models.IntegerField(
        blank=True, null=True,
        help_text='50.0 percent or more')
    B25070_011E = models.IntegerField(
        blank=True, null=True,
        help_text='Not computed')

    # B25075 - Value
    B25075_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Value: Total:')
    B25075_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Less than $10,000')
    B25075_003E = models.IntegerField(
        blank=True, null=True,
        help_text='$10,000 to $14,999')
    B25075_004E = models.IntegerField(
        blank=True, null=True,
        help_text='$15,000 to $19,999')
    B25075_005E = models.IntegerField(
        blank=True, null=True,
        help_text='$20,000 to $24,999')
    B25075_006E = models.IntegerField(
        blank=True, null=True,
        help_text='$25,000 to $29,999')
    B25075_007E = models.IntegerField(
        blank=True, null=True,
        help_text='$30,000 to $34,999')
    B25075_008E = models.IntegerField(
        blank=True, null=True,
        help_text='$35,000 to $39,999')
    B25075_009E = models.IntegerField(
        blank=True, null=True,
        help_text='$40,000 to $49,999')
    B25075_010E = models.IntegerField(
        blank=True, null=True,
        help_text='$50,000 to $59,999')
    B25075_011E = models.IntegerField(
        blank=True, null=True,
        help_text='$60,000 to $69,999')
    B25075_012E = models.IntegerField(
        blank=True, null=True,
        help_text='$70,000 to $79,999')
    B25075_013E = models.IntegerField(
        blank=True, null=True,
        help_text='$80,000 to $89,999')
    B25075_014E = models.IntegerField(
        blank=True, null=True,
        help_text='$90,000 to $99,999')
    B25075_015E = models.IntegerField(
        blank=True, null=True,
        help_text='$100,000 to $124,999')
    B25075_016E = models.IntegerField(
        blank=True, null=True,
        help_text='$125,000 to $149,999')
    B25075_017E = models.IntegerField(
        blank=True, null=True,
        help_text='$150,000 to $174,999')
    B25075_018E = models.IntegerField(
        blank=True, null=True,
        help_text='$175,000 to $199,999')
    B25075_019E = models.IntegerField(
        blank=True, null=True,
        help_text='$200,000 to $249,999')
    B25075_020E = models.IntegerField(
        blank=True, null=True,
        help_text='$250,000 to $299,999')
    B25075_021E = models.IntegerField(
        blank=True, null=True,
        help_text='$300,000 to $399,999')
    B25075_022E = models.IntegerField(
        blank=True, null=True,
        help_text='$400,000 to $499,999')
    B25075_023E = models.IntegerField(
        blank=True, null=True,
        help_text='$500,000 to $749,999')
    B25075_024E = models.IntegerField(
        blank=True, null=True,
        help_text='$750,000 to $999,999')
    B25075_025E = models.IntegerField(
        blank=True, null=True,
        help_text='$1,000,000 or more')

    # B25091 - Mortgage Status by Selected Monthly Owner Costs As a
    #          Percentage of Household Income In the Past 12 Months
    B25091_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Mortgage Status by Selected Monthly Owner Costs As a Percentage'
            ' of Household Income In the Past 12 Months: Total:'))
    B25091_002E = models.IntegerField(
        blank=True, null=True,
        help_text='Housing units with a mortgage:')
    B25091_003E = models.IntegerField(
        blank=True, null=True,
        help_text='Less than 10.0 percent')
    B25091_004E = models.IntegerField(
        blank=True, null=True,
        help_text='10.0 to 14.9 percent')
    B25091_005E = models.IntegerField(
        blank=True, null=True,
        help_text='15.0 to 19.9 percent')
    B25091_006E = models.IntegerField(
        blank=True, null=True,
        help_text='20.0 to 24.9 percent')
    B25091_007E = models.IntegerField(
        blank=True, null=True,
        help_text='25.0 to 29.9 percent')
    B25091_008E = models.IntegerField(
        blank=True, null=True,
        help_text='30.0 to 34.9 percent')
    B25091_009E = models.IntegerField(
        blank=True, null=True,
        help_text='35.0 to 39.9 percent')
    B25091_010E = models.IntegerField(
        blank=True, null=True,
        help_text='40.0 to 49.9 percent')
    B25091_011E = models.IntegerField(
        blank=True, null=True,
        help_text='50.0 percent or more')
    B25091_012E = models.IntegerField(
        blank=True, null=True,
        help_text='Not computed')
    B25091_013E = models.IntegerField(
        blank=True, null=True,
        help_text='Housing units without a mortgage:')
    B25091_014E = models.IntegerField(
        blank=True, null=True,
        help_text='Less than 10.0 percent')
    B25091_015E = models.IntegerField(
        blank=True, null=True,
        help_text='10.0 to 14.9 percent')
    B25091_016E = models.IntegerField(
        blank=True, null=True,
        help_text='15.0 to 19.9 percent')
    B25091_017E = models.IntegerField(
        blank=True, null=True,
        help_text='20.0 to 24.9 percent')
    B25091_018E = models.IntegerField(
        blank=True, null=True,
        help_text='25.0 to 29.9 percent')
    B25091_019E = models.IntegerField(
        blank=True, null=True,
        help_text='30.0 to 34.9 percent')
    B25091_020E = models.IntegerField(
        blank=True, null=True,
        help_text='35.0 to 39.9 percent')
    B25091_021E = models.IntegerField(
        blank=True, null=True,
        help_text='40.0 to 49.9 percent')
    B25091_022E = models.IntegerField(
        blank=True, null=True,
        help_text='50.0 percent or more')
    B25091_023E = models.IntegerField(
        blank=True, null=True,
        help_text='Not computed')
