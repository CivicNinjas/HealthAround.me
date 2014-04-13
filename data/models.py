from django.db import models
from boundaryservice.models import Boundary


class Census(models.Model):
    '''Selected items from U.S. Census 5-Year Summary for Boundary'''

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    logical_num = models.IntegerField(help_text='Logical record number')

    # B01001 - Sex by Age
    B01001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Sex by Age: Total:')
    B01001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B01001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B01001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 9 years')
    B01001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='10 to 14 years')
    B01001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B01001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 and 19 years')
    B01001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 years')
    B01001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='21 years')
    B01001_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='22 to 24 years')
    B01001_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 29 years')
    B01001_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='30 to 34 years')
    B01001_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 39 years')
    B01001_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='40 to 44 years')
    B01001_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 49 years')
    B01001_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='50 to 54 years')
    B01001_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 59 years')
    B01001_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='60 and 61 years')
    B01001_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='62 to 64 years')
    B01001_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 and 66 years')
    B01001_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='67 to 69 years')
    B01001_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='70 to 74 years')
    B01001_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 to 79 years')
    B01001_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='80 to 84 years')
    B01001_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='85 years and over')
    B01001_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B01001_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B01001_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 9 years')
    B01001_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='10 to 14 years')
    B01001_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B01001_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 and 19 years')
    B01001_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 years')
    B01001_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='21 years')
    B01001_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='22 to 24 years')
    B01001_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 29 years')
    B01001_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='30 to 34 years')
    B01001_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 39 years')
    B01001_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='40 to 44 years')
    B01001_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 49 years')
    B01001_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='50 to 54 years')
    B01001_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 59 years')
    B01001_042E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='60 and 61 years')
    B01001_043E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='62 to 64 years')
    B01001_044E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 and 66 years')
    B01001_045E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='67 to 69 years')
    B01001_046E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='70 to 74 years')
    B01001_047E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 to 79 years')
    B01001_048E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='80 to 84 years')
    B01001_049E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='85 years and over')

    # B01002 - Median Age by Sex
    B01002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Median Age by Sex: Total:')
    B01002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B01002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')

    # B01003 - Total Population
    B01003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Total Population: Total')

    # B02001 - Race
    B02001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Race: Total:')
    B02001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='White alone')
    B02001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Black or African American alone')
    B02001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='American Indian and Alaska Native alone')
    B02001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Asian alone')
    B02001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Native Hawaiian and Other Pacific Islander alone')
    B02001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some other race alone')
    B02001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Two or more races:')
    B02001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Two races including Some other race')
    B02001_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Two races excluding Some other race, and three or more races'))

    # B07003 - Geographical Mobility In the Past Year by Sex For
    #          Current Residence In the United States
    B07003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Geographical Mobility In the Past Year by Sex For Current'
            ' Residence In the United States: Total:'))
    B07003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')
    B07003_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Same house 1 year ago:')
    B07003_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')
    B07003_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Moved within same county:')
    B07003_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')
    B07003_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Moved from different county within same state:')
    B07003_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')
    B07003_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Moved from different state:')
    B07003_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')
    B07003_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Moved from abroad:')
    B07003_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B07003_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')

    # B08016 - Place of Work For Workers 16 Years And
    #          Over--Metropolitan Statistical Area Level
    B08016_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Place of Work For Workers 16 Years And Over--Metropolitan'
            ' Statistical Area Level: Total:'))
    B08016_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Living in a principal city:')
    B08016_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in Metropolitan Statistical Area of residence:')
    B08016_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a different Metropolitan Statistical Area:')
    B08016_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a Micropolitan Statistical Area:')
    B08016_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Worked outside any Metropolitan or Micropolitan Statistical'
            ' Area'))
    B08016_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Living outside any principal city:')
    B08016_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in Metropolitan Statistical Area of residence:')
    B08016_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a different Metropolitan Statistical Area:')
    B08016_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a Micropolitan Statistical Area:')
    B08016_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08016_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08016_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Worked outside any Metropolitan or Micropolitan Statistical'
            ' Area'))

    # B08018 - Place of Work For Workers 16 Years And Over--Not
    #          Metropolitan Or Micropolitan Statistical Area Level
    B08018_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Place of Work For Workers 16 Years And Over--Not Metropolitan'
            ' Or Micropolitan Statistical Area Level: Total:'))
    B08018_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a Metropolitan Statistical Area:')
    B08018_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08018_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08018_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a Micropolitan Statistical Area:')
    B08018_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked in a principal city')
    B08018_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked outside any principal city')
    B08018_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Worked outside any Metropolitan or Micropolitan Statistical'
            ' Area'))

    # B08301 - Means of Transportation to Work
    B08301_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Means of Transportation to Work: Total:')
    B08301_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Car, truck, or van:')
    B08301_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Drove alone')
    B08301_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Carpooled:')
    B08301_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In 2-person carpool')
    B08301_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In 3-person carpool')
    B08301_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In 4-person carpool')
    B08301_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In 5- or 6-person carpool')
    B08301_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In 7-or-more-person carpool')
    B08301_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public transportation (excluding taxicab):')
    B08301_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bus or trolley bus')
    B08301_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Streetcar or trolley car (carro publico in Puerto Rico)')
    B08301_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Subway or elevated')
    B08301_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Railroad')
    B08301_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Ferryboat')
    B08301_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Taxicab')
    B08301_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Motorcycle')
    B08301_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bicycle')
    B08301_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Walked')
    B08301_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other means')
    B08301_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Worked at home')

    # B08303 - Travel Time to Work
    B08303_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Travel Time to Work: Total:')
    B08303_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than 5 minutes')
    B08303_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 9 minutes')
    B08303_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='10 to 14 minutes')
    B08303_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 minutes')
    B08303_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 24 minutes')
    B08303_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 29 minutes')
    B08303_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='30 to 34 minutes')
    B08303_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 39 minutes')
    B08303_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='40 to 44 minutes')
    B08303_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 59 minutes')
    B08303_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='60 to 89 minutes')
    B08303_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='90 or more minutes')

    # B11001 - Household Type (Including Living Alone)
    B11001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Household Type (Including Living Alone): Total:')
    B11001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Family households:')
    B11001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family')
    B11001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B11001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present')
    B11001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present')
    B11001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nonfamily households:')
    B11001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder living alone')
    B11001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder not living alone')

    # B12503 - Divorces In the Last Year by Sex by Marital Status For
    #          the Population 15 Years And Over
    B12503_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Divorces In the Last Year by Sex by Marital Status For the'
            ' Population 15 Years And Over: Total:'))
    B12503_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B12503_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Never married')
    B12503_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Ever married:')
    B12503_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Divorced last year')
    B12503_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not divorced last year')
    B12503_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B12503_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Never married')
    B12503_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Ever married:')
    B12503_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Divorced last year')
    B12503_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not divorced last year')

    # B13001 - Marital Status by Age For Women 15 to 50 Years
    B13001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Marital Status by Age For Women 15 to 50 Years: Total:')
    B13001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Now married (including spouse absent):')
    B13001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years')
    B13001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years')
    B13001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years')
    B13001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unmarried (never married, widowed, and divorced):')
    B13001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years')
    B13001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years')
    B13001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years')

    # B13002 - Women 15 to 50 Years Who Had a Birth In the Past 12
    #          Months by Marital Status And Age
    B13002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Women 15 to 50 Years Who Had a Birth In the Past 12 Months by'
            ' Marital Status And Age: Total:'))
    B13002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Women who had a birth in the past 12 months:')
    B13002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Now married (including separated and spouse absent):')
    B13002_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years old')
    B13002_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years old')
    B13002_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years old')
    B13002_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unmarried (never married, widowed, and divorced):')
    B13002_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years old')
    B13002_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years old')
    B13002_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years old')
    B13002_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Women who did not have a birth in the past 12 months:')
    B13002_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Now married (including separated and spouse absent):')
    B13002_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years old')
    B13002_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years old')
    B13002_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years old')
    B13002_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unmarried (never married, widowed, and divorced):')
    B13002_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 19 years old')
    B13002_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='20 to 34 years old')
    B13002_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 50 years old')

    # B13004 - Women 15 to 50 Years Who Had a Birth In the Past 12
    #          Months by Marital Status And Presence of Unmarried
    #          Partner
    B13004_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Women 15 to 50 Years Who Had a Birth In the Past 12 Months by'
            ' Marital Status And Presence of Unmarried Partner: Total:'))
    B13004_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Women who had a birth in the past 12 months:')
    B13004_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Now married (including separated and spouse absent)')
    B13004_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unmarried (never married, widowed and divorced):')
    B13004_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Partner in an unmarried partner household')
    B13004_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not an unmarried partner')
    B13004_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Women who did not have a birth in the past 12 months:')
    B13004_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Now married (including separated and spouse absent)')
    B13004_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unmarried (never married, widowed and divorced):')
    B13004_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Partner in an unmarried partner household')
    B13004_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not an unmarried partner')

    # B14001 - School Enrollment by Level of School For the Population
    #          3 Years And Over
    B14001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'School Enrollment by Level of School For the Population 3 Years'
            ' And Over: Total:'))
    B14001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in school:')
    B14001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in nursery school, preschool')
    B14001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in kindergarten')
    B14001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 1 to grade 4')
    B14001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 5 to grade 8')
    B14001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 9 to grade 12')
    B14001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in college, undergraduate years')
    B14001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Graduate or professional school')
    B14001_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in school')

    # B14002 - Sex by School Enrollment by Level of School by Type of
    #          School For the Population 3 Years And Over
    B14002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Sex by School Enrollment by Level of School by Type of School'
            ' For the Population 3 Years And Over: Total:'))
    B14002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B14002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in school:')
    B14002_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in nursery school, preschool:')
    B14002_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in kindergarten:')
    B14002_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 1 to grade 4:')
    B14002_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 5 to grade 8:')
    B14002_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 9 to grade 12:')
    B14002_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in college undergraduate years:')
    B14002_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in graduate or professional school:')
    B14002_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in school')
    B14002_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B14002_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in school:')
    B14002_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in nursery school, preschool:')
    B14002_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in kindergarten:')
    B14002_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 1 to grade 4:')
    B14002_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 5 to grade 8:')
    B14002_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 9 to grade 12:')
    B14002_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_042E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_043E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in college undergraduate years:')
    B14002_044E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_045E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_046E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in graduate or professional school:')
    B14002_047E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public school')
    B14002_048E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private school')
    B14002_049E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in school')

    # B14004 - Sex by College Or Graduate School Enrollment by Type of
    #          School by Age For the Population 15 Years And Over
    B14004_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Sex by College Or Graduate School Enrollment by Type of School'
            ' by Age For the Population 15 Years And Over: Total:'))
    B14004_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B14004_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in public college or graduate school:')
    B14004_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')
    B14004_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in private college or graduate school:')
    B14004_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')
    B14004_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in college or graduate school:')
    B14004_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')
    B14004_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B14004_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in public college or graduate school:')
    B14004_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')
    B14004_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in private college or graduate school:')
    B14004_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')
    B14004_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in college or graduate school:')
    B14004_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 to 17 years')
    B14004_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B14004_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B14004_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 years and over')

    # B14007 - School Enrollment by Detailed Level of School For the
    #          Population 3 Years And Over
    B14007_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'School Enrollment by Detailed Level of School For the'
            ' Population 3 Years And Over: Total:'))
    B14007_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in school:')
    B14007_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in nursery school, preschool')
    B14007_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in kindergarten')
    B14007_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 1')
    B14007_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 2')
    B14007_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 3')
    B14007_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 4')
    B14007_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 5')
    B14007_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 6')
    B14007_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 7')
    B14007_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 8')
    B14007_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 9')
    B14007_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 10')
    B14007_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 11')
    B14007_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in grade 12')
    B14007_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Enrolled in college, undergraduate years')
    B14007_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Graduate or professional school')
    B14007_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not enrolled in school')

    # B15003 - Educational Attainment For the Population 25 Years And Over
    B15003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Educational Attainment For the Population 25 Years And Over:'
            ' Total:'))
    B15003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No schooling completed')
    B15003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nursery school')
    B15003_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Kindergarten')
    B15003_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='1st grade')
    B15003_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='2nd grade')
    B15003_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='3rd grade')
    B15003_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='4th grade')
    B15003_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5th grade')
    B15003_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6th grade')
    B15003_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='7th grade')
    B15003_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='8th grade')
    B15003_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='9th grade')
    B15003_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='10th grade')
    B15003_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='11th grade')
    B15003_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='12th grade, no diploma')
    B15003_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Regular high school diploma')
    B15003_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='GED or alternative credential')
    B15003_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, less than 1 year')
    B15003_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, 1 or more years, no degree')
    B15003_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Associate\'s degree')
    B15003_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bachelor\'s degree')
    B15003_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Master\'s degree')
    B15003_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Professional school degree')
    B15003_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Doctorate degree')

    # B17001 - Poverty Status In the Past 12 Months by Sex by Age
    B17001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Poverty Status In the Past 12 Months by Sex by Age: Total:')
    B17001_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months below poverty level:')
    B17001_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B17001_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B17001_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 years')
    B17001_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 11 years')
    B17001_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='12 to 14 years')
    B17001_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 years')
    B17001_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='16 and 17 years')
    B17001_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B17001_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B17001_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years')
    B17001_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years')
    B17001_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years')
    B17001_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years')
    B17001_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over')
    B17001_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B17001_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B17001_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 years')
    B17001_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 11 years')
    B17001_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='12 to 14 years')
    B17001_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 years')
    B17001_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='16 and 17 years')
    B17001_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B17001_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B17001_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years')
    B17001_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years')
    B17001_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years')
    B17001_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years')
    B17001_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over')
    B17001_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level:')
    B17001_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B17001_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B17001_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 years')
    B17001_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 11 years')
    B17001_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='12 to 14 years')
    B17001_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 years')
    B17001_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='16 and 17 years')
    B17001_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B17001_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B17001_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years')
    B17001_042E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years')
    B17001_043E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years')
    B17001_044E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years')
    B17001_045E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over')
    B17001_046E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B17001_047E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years')
    B17001_048E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 years')
    B17001_049E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 11 years')
    B17001_050E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='12 to 14 years')
    B17001_051E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='15 years')
    B17001_052E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='16 and 17 years')
    B17001_053E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years')
    B17001_054E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years')
    B17001_055E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years')
    B17001_056E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years')
    B17001_057E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years')
    B17001_058E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years')
    B17001_059E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over')

    # B17003 - Poverty Status In the Past 12 Months of Individuals by
    #          Sex by Educational Attainment
    B17003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Poverty Status In the Past 12 Months of Individuals by Sex by'
            ' Educational Attainment: Total:'))
    B17003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months below poverty level:')
    B17003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B17003_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than high school graduate')
    B17003_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='High school graduate (includes equivalency)')
    B17003_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, associate\'s degree')
    B17003_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bachelor\'s degree or higher')
    B17003_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B17003_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than high school graduate')
    B17003_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='High school graduate (includes equivalency)')
    B17003_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, associate\'s degree')
    B17003_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bachelor\'s degree or higher')
    B17003_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level:')
    B17003_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B17003_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than high school graduate')
    B17003_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='High school graduate (includes equivalency)')
    B17003_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, associate\'s degree')
    B17003_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bachelor\'s degree or higher')
    B17003_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B17003_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than high school graduate')
    B17003_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='High school graduate (includes equivalency)')
    B17003_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Some college, associate\'s degree')
    B17003_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Bachelor\'s degree or higher')

    # B17010 - Poverty Status In the Past 12 Months of Families by
    #          Family Type by Presence of Related Children Under 18
    #          Years by Age of Related Children
    B17010_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Poverty Status In the Past 12 Months of Families by Family Type'
            ' by Presence of Related Children Under 18 Years by Age of'
            ' Related Children: Total:'))
    B17010_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months below poverty level:')
    B17010_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family:')
    B17010_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')
    B17010_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B17010_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present:')
    B17010_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')
    B17010_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present:')
    B17010_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')
    B17010_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level:')
    B17010_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family:')
    B17010_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')
    B17010_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B17010_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present:')
    B17010_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')
    B17010_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present:')
    B17010_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With related children under 18 years:')
    B17010_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years only')
    B17010_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years and 5 to 17 years')
    B17010_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years only')
    B17010_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No related children under 18 years')

    # B18101 - Sex by Age by Disability Status
    B18101_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Sex by Age by Disability Status: Total:')
    B18101_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B18101_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years:')
    B18101_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years:')
    B18101_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 34 years:')
    B18101_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 64 years:')
    B18101_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B18101_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B18101_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B18101_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 5 years:')
    B18101_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='5 to 17 years:')
    B18101_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 34 years:')
    B18101_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 64 years:')
    B18101_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B18101_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')
    B18101_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B18101_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability')
    B18101_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability')

    # B18135 - Age by Disability Status by Health Insurance Coverage Status
    B18135_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Age by Disability Status by Health Insurance Coverage Status:'
            ' Total:'))
    B18135_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 18 years:')
    B18135_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability:')
    B18135_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')
    B18135_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability:')
    B18135_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')
    B18135_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 64 years:')
    B18135_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability:')
    B18135_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')
    B18135_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability:')
    B18135_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')
    B18135_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 years and over:')
    B18135_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With a disability:')
    B18135_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')
    B18135_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No disability:')
    B18135_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With health insurance coverage:')
    B18135_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance coverage')
    B18135_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public health coverage')
    B18135_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No health insurance coverage')

    # B19013 - Median Household Income In the Past 12 Months (In 2012
    #          Inflation-Adjusted Dollars)
    B19013_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Median household income in the past 12 months (in 2012'
            ' inflation-adjusted dollars)'))

    # B19055 - Social Security Income In the Past 12 Months For Households
    B19055_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Social Security Income In the Past 12 Months For Households:'
            ' Total:'))
    B19055_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Social Security income')
    B19055_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Social Security income')

    # B19056 - Supplemental Security Income (Ssi) In the Past 12 Months
    #          For Households
    B19056_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Supplemental Security Income (Ssi) In the Past 12 Months For'
            ' Households: Total:'))
    B19056_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Supplemental Security Income (SSI)')
    B19056_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Supplemental Security Income (SSI)')

    # B19057 - Public Assistance Income In the Past 12 Months For Households
    B19057_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Public Assistance Income In the Past 12 Months For Households:'
            ' Total:'))
    B19057_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public assistance income')
    B19057_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public assistance income')

    # B19058 - Public Assistance Income Or Food Stamps/Snap In the Past
    #          12 Months For Households
    B19058_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Public Assistance Income Or Food Stamps/Snap In the Past 12'
            ' Months For Households: Total:'))
    B19058_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With cash public assistance or Food Stamps/SNAP')
    B19058_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No cash public assistance or Food Stamps/SNAP')

    # B19083 - Gini Index of Income Inequality
    B19083_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Gini Index of Income Inequality: Gini Index')

    # B19113 - Median Family Income In the Past 12 Months (In 2012
    #          Inflation-Adjusted Dollars)
    B19113_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Median family income in the past 12 months (in 2012'
            ' inflation-adjusted dollars)'))

    # B19301 - Per Capita Income In the Past 12 Months (In 2012
    #          Inflation-Adjusted Dollars)
    B19301_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Per capita income in the past 12 months (in 2012'
            ' inflation-adjusted dollars)'))

    # B22002 - Receipt of Food Stamps/Snap In the Past 12 Months by
    #          Presence of Children Under 18 Years by Household Type
    #          For Households
    B22002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Receipt of Food Stamps/Snap In the Past 12 Months by Presence'
            ' of Children Under 18 Years by Household Type For Households:'
            ' Total:'))
    B22002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Household received Food Stamps/SNAP in the past 12 months:')
    B22002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With children under 18 years:')
    B22002_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family')
    B22002_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B22002_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present')
    B22002_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present')
    B22002_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nonfamily households')
    B22002_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No children under 18 years:')
    B22002_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family')
    B22002_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B22002_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present')
    B22002_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present')
    B22002_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nonfamily households')
    B22002_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Household did not receive Food Stamps/SNAP in the past 12'
            ' months:'))
    B22002_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With children under 18 years:')
    B22002_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family')
    B22002_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B22002_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present')
    B22002_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present')
    B22002_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nonfamily households')
    B22002_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No children under 18 years:')
    B22002_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Married-couple family')
    B22002_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Other family:')
    B22002_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male householder, no wife present')
    B22002_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female householder, no husband present')
    B22002_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Nonfamily households')

    # B22003 - Receipt of Food Stamps/Snap In the Past 12 Months by
    #          Poverty Status In the Past 12 Months For Households
    B22003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Receipt of Food Stamps/Snap In the Past 12 Months by Poverty'
            ' Status In the Past 12 Months For Households: Total:'))
    B22003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Household received Food Stamps/SNAP in the past 12 months:')
    B22003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months below poverty level')
    B22003_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level')
    B22003_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Household did not receive Food Stamps/SNAP in the past 12'
            ' months:'))
    B22003_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months below poverty level')
    B22003_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Income in the past 12 months at or above poverty level')

    # B23020 - Mean Usual Hours Worked In the Past 12 Months For
    #          Workers 16 to 64 Years
    B23020_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Mean Usual Hours Worked In the Past 12 Months For Workers 16 to'
            ' 64 Years: Total:'))
    B23020_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B23020_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female')

    # B23025 - Employment Status For the Population 16 Years And Over
    B23025_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Employment Status For the Population 16 Years And Over: Total:'))
    B23025_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='In labor force:')
    B23025_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Civilian labor force:')
    B23025_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Employed')
    B23025_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Unemployed')
    B23025_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Armed Forces')
    B23025_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Not in labor force')

    # B25001 - Housing Units
    B25001_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Housing Units: Total')

    # B25002 - Occupancy Status
    B25002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Occupancy Status: Total:')
    B25002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Occupied')
    B25002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Vacant')

    # B25003 - Tenure
    B25003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Tenure: Total:')
    B25003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Owner occupied')
    B25003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Renter occupied')

    # B25027 - Mortgage Status by Age of Householder
    B25027_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Mortgage Status by Age of Householder: Total:')
    B25027_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Housing units with a mortgage:')
    B25027_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 15 to 34 years')
    B25027_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 35 to 44 years')
    B25027_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 45 to 54 years')
    B25027_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 55 to 59 years')
    B25027_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 60 to 64 years')
    B25027_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 65 to 74 years')
    B25027_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 75 years and over')
    B25027_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Housing units without a mortgage:')
    B25027_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 15 to 34 years')
    B25027_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 35 to 44 years')
    B25027_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 45 to 54 years')
    B25027_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 55 to 59 years')
    B25027_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 60 to 64 years')
    B25027_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 65 to 74 years')
    B25027_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Householder 75 years and over')

    # B25034 - Year Structure Built
    B25034_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Year Structure Built: Total:')
    B25034_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 2010 or later')
    B25034_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 2000 to 2009')
    B25034_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1990 to 1999')
    B25034_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1980 to 1989')
    B25034_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1970 to 1979')
    B25034_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1960 to 1969')
    B25034_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1950 to 1959')
    B25034_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1940 to 1949')
    B25034_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Built 1939 or earlier')

    # B25035 - Median Year Structure Built
    B25035_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Median year structure built')

    # B25058 - Median Contract Rent (Dollars)
    B25058_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Median Contract Rent (Dollars): Median contract rent')

    # B25064 - Median Gross Rent (Dollars)
    B25064_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Median Gross Rent (Dollars): Median gross rent')

    # B25075 - Value
    B25075_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Value: Total:')
    B25075_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than $10,000')
    B25075_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$10,000 to $14,999')
    B25075_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$15,000 to $19,999')
    B25075_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$20,000 to $24,999')
    B25075_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$25,000 to $29,999')
    B25075_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$30,000 to $34,999')
    B25075_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$35,000 to $39,999')
    B25075_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$40,000 to $49,999')
    B25075_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$50,000 to $59,999')
    B25075_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$60,000 to $69,999')
    B25075_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$70,000 to $79,999')
    B25075_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$80,000 to $89,999')
    B25075_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$90,000 to $99,999')
    B25075_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$100,000 to $124,999')
    B25075_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$125,000 to $149,999')
    B25075_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$150,000 to $174,999')
    B25075_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$175,000 to $199,999')
    B25075_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$200,000 to $249,999')
    B25075_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$250,000 to $299,999')
    B25075_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$300,000 to $399,999')
    B25075_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$400,000 to $499,999')
    B25075_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$500,000 to $749,999')
    B25075_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$750,000 to $999,999')
    B25075_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$1,000,000 or more')

    # B25087 - Mortgage Status And Selected Monthly Owner Costs
    B25087_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Mortgage Status And Selected Monthly Owner Costs: Total:')
    B25087_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Housing units with a mortgage:')
    B25087_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than $200')
    B25087_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$200 to $299')
    B25087_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$300 to $399')
    B25087_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$400 to $499')
    B25087_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$500 to $599')
    B25087_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$600 to $699')
    B25087_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$700 to $799')
    B25087_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$800 to $899')
    B25087_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$900 to $999')
    B25087_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$1,000 to $1,249')
    B25087_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$1,250 to $1,499')
    B25087_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$1,500 to $1,999')
    B25087_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$2,000 to $2,499')
    B25087_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$2,500 to $2,999')
    B25087_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$3,000 or more')
    B25087_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Housing units without a mortgage:')
    B25087_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Less than $100')
    B25087_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$100 to $149')
    B25087_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$150 to $199')
    B25087_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$200 to $249')
    B25087_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$250 to $299')
    B25087_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$300 to $349')
    B25087_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$350 to $399')
    B25087_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$400 to $499')
    B25087_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$500 to $599')
    B25087_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$600 to $699')
    B25087_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='$700 or more')

    # B27002 - Private Health Insurance Status by Sex by Age
    B27002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Private Health Insurance Status by Sex by Age: Total:')
    B27002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B27002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 6 years:')
    B27002_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 17 years:')
    B27002_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years:')
    B27002_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years:')
    B27002_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years:')
    B27002_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years:')
    B27002_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years:')
    B27002_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B27002_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B27002_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B27002_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 6 years:')
    B27002_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 17 years:')
    B27002_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years:')
    B27002_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years:')
    B27002_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_042E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_043E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years:')
    B27002_044E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_045E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_046E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years:')
    B27002_047E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_048E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_049E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years:')
    B27002_050E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_051E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_052E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B27002_053E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_054E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')
    B27002_055E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B27002_056E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With private health insurance')
    B27002_057E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No private health insurance')

    # B27003 - Public Health Insurance Status by Sex by Age
    B27003_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Public Health Insurance Status by Sex by Age: Total:')
    B27003_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    B27003_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 6 years:')
    B27003_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 17 years:')
    B27003_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years:')
    B27003_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years:')
    B27003_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years:')
    B27003_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years:')
    B27003_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years:')
    B27003_022E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_023E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_024E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B27003_025E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_026E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_027E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B27003_028E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_029E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_030E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    B27003_031E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 6 years:')
    B27003_032E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_033E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_034E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='6 to 17 years:')
    B27003_035E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_036E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_037E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 24 years:')
    B27003_038E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_039E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_040E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='25 to 34 years:')
    B27003_041E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_042E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_043E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='35 to 44 years:')
    B27003_044E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_045E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_046E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='45 to 54 years:')
    B27003_047E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_048E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_049E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='55 to 64 years:')
    B27003_050E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_051E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_052E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 to 74 years:')
    B27003_053E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_054E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')
    B27003_055E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='75 years and over:')
    B27003_056E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With public coverage')
    B27003_057E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No public coverage')

    # C17002 - Ratio of Income to Poverty Level In the Past 12 Months
    C17002_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Ratio of Income to Poverty Level In the Past 12 Months: Total:'))
    C17002_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under .50')
    C17002_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='.50 to .99')
    C17002_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='1.00 to 1.24')
    C17002_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='1.25 to 1.49')
    C17002_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='1.50 to 1.84')
    C17002_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='1.85 to 1.99')
    C17002_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='2.00 and over')

    # C27006 - Medicare Coverage by Sex by Age
    C27006_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Medicare Coverage by Sex by Age: Total:')
    C27006_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    C27006_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 18 years:')
    C27006_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')
    C27006_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 64 years:')
    C27006_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')
    C27006_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 years and over:')
    C27006_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')
    C27006_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    C27006_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 18 years:')
    C27006_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')
    C27006_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 64 years:')
    C27006_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')
    C27006_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 years and over:')
    C27006_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicare coverage')
    C27006_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicare coverage')

    # C27007 - Medicaid/Means-Tested Public Coverage by Sex by Age
    C27007_001E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text=(
            'Medicaid/Means-Tested Public Coverage by Sex by Age: Total:'))
    C27007_002E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Male:')
    C27007_003E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 18 years:')
    C27007_004E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_005E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
    C27007_006E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 64 years:')
    C27007_007E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_008E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
    C27007_009E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 years and over:')
    C27007_010E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_011E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
    C27007_012E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Female:')
    C27007_013E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='Under 18 years:')
    C27007_014E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_015E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
    C27007_016E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='18 to 64 years:')
    C27007_017E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_018E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
    C27007_019E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='65 years and over:')
    C27007_020E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='With Medicaid/means-tested public coverage')
    C27007_021E = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True,
        help_text='No Medicaid/means-tested public coverage')
