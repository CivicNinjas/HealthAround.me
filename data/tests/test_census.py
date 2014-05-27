from django.test import TestCase
import StringIO
import mock

from data.census.loading import CensusLoader


# Subset of the Sequence_Number_and_Table_Number_Lookup.txt (SNATNL) file
sample_sequence = '''\
File ID,Table ID,Sequence Number,Line Number,Start Position,\
Total Cells in Table,Total Cells in Sequence,Table Title,Subject Area
ACSSF,B00001,0001, ,7,1 CELL, ,UNWEIGHTED SAMPLE COUNT OF THE POPULATION,\
Unweighted Count
ACSSF,B00001,0001, , ,, ,Universe:  Total population,
ACSSF,B00001,0001,1, ,, ,Total,
ACSSF,B00002,0001, ,8,1 CELL,2,UNWEIGHTED SAMPLE HOUSING UNITS,Unweighted Count
ACSSF,B00002,0001, , ,, ,Universe:  Housing units,
ACSSF,B00002,0001,1, ,, ,Total,
ACSSF,B01001,0002, ,7,49 CELLS, ,SEX BY AGE,Age-Sex
ACSSF,B01001,0002, , ,, ,Universe:  Total population,
ACSSF,B01001,0002,1, ,, ,Total:,
ACSSF,B01001,0002,2, ,, ,Male:,
ACSSF,B01001,0002,3, ,, ,Under 5 years,
ACSSF,B01001,0002,4, ,, ,5 to 9 years,
ACSSF,B01001,0002,5, ,, ,10 to 14 years,
ACSSF,B01001,0002,6, ,, ,15 to 17 years,
ACSSF,B01001,0002,7, ,, ,18 and 19 years,
ACSSF,B01001,0002,8, ,, ,20 years,
ACSSF,B01001,0002,9, ,, ,21 years,
ACSSF,B01001,0002,10, ,, ,22 to 24 years,
ACSSF,B01001,0002,11, ,, ,25 to 29 years,
ACSSF,B01001,0002,12, ,, ,30 to 34 years,
ACSSF,B01001,0002,13, ,, ,35 to 39 years,
ACSSF,B01001,0002,14, ,, ,40 to 44 years,
ACSSF,B01001,0002,15, ,, ,45 to 49 years,
ACSSF,B01001,0002,16, ,, ,50 to 54 years,
ACSSF,B01001,0002,17, ,, ,55 to 59 years,
ACSSF,B01001,0002,18, ,, ,60 and 61 years,
ACSSF,B01001,0002,19, ,, ,62 to 64 years,
ACSSF,B01001,0002,20, ,, ,65 and 66 years,
ACSSF,B01001,0002,21, ,, ,67 to 69 years,
ACSSF,B01001,0002,22, ,, ,70 to 74 years,
ACSSF,B01001,0002,23, ,, ,75 to 79 years,
ACSSF,B01001,0002,24, ,, ,80 to 84 years,
ACSSF,B01001,0002,25, ,, ,85 years and over,
ACSSF,B01001,0002,26, ,, ,Female:,
ACSSF,B01001,0002,27, ,, ,Under 5 years,
ACSSF,B01001,0002,28, ,, ,5 to 9 years,
ACSSF,B01001,0002,29, ,, ,10 to 14 years,
ACSSF,B01001,0002,30, ,, ,15 to 17 years,
ACSSF,B01001,0002,31, ,, ,18 and 19 years,
ACSSF,B01001,0002,32, ,, ,20 years,
ACSSF,B01001,0002,33, ,, ,21 years,
ACSSF,B01001,0002,34, ,, ,22 to 24 years,
ACSSF,B01001,0002,35, ,, ,25 to 29 years,
ACSSF,B01001,0002,36, ,, ,30 to 34 years,
ACSSF,B01001,0002,37, ,, ,35 to 39 years,
ACSSF,B01001,0002,38, ,, ,40 to 44 years,
ACSSF,B01001,0002,39, ,, ,45 to 49 years,
ACSSF,B01001,0002,40, ,, ,50 to 54 years,
ACSSF,B01001,0002,41, ,, ,55 to 59 years,
ACSSF,B01001,0002,42, ,, ,60 and 61 years,
ACSSF,B01001,0002,43, ,, ,62 to 64 years,
ACSSF,B01001,0002,44, ,, ,65 and 66 years,
ACSSF,B01001,0002,45, ,, ,67 to 69 years,
ACSSF,B01001,0002,46, ,, ,70 to 74 years,
ACSSF,B01001,0002,47, ,, ,75 to 79 years,
ACSSF,B01001,0002,48, ,, ,80 to 84 years,
ACSSF,B01001,0002,49, ,, ,85 years and over,
ACSSF,B01002,0003, ,100,3 CELLS, ,MEDIAN AGE BY SEX,Age-Sex
ACSSF,B01002,0003, , ,, ,Universe:  Total population,
ACSSF,B01002,0003,0.5, ,, ,Median age --,
ACSSF,B01002,0003,1, ,, ,Total:,
ACSSF,B01002,0003,2, ,, ,Male,
ACSSF,B01002,0003,3, ,, ,Female,
ACSSF,B19113,0063, ,75,1 CELL, ,MEDIAN FAMILY INCOME IN THE PAST 12 MONTHS\
 (IN 2012 INFLATION-ADJUSTED DOLLARS),Income
ACSSF,B19113,0063, , ,, ,Universe:  Families,
ACSSF,B19113,0063,1, ,, ,Median family income in the past 12 months\
 (in 2012 inflation-adjusted dollars),
'''


class CensusLoaderTest(TestCase):
    maxDiff = None

    def getCensusLoaderForSeq(self, table_ids):
        cl = CensusLoader(table_ids, [])
        cl.open_snatnl = mock.MagicMock(name='open_snatnl')
        cl.open_snatnl.return_value = StringIO.StringIO(sample_sequence)
        return cl

    def test_seq_defs_two_tables_in_one_seq_file(self):
        table_ids = {
            'B00002': {},
            'B00001': {},
        }
        cl = self.getCensusLoaderForSeq(table_ids)
        cl.open_snatnl = mock.MagicMock(name='open_snatnl')
        cl.open_snatnl.return_value = StringIO.StringIO(sample_sequence)
        sd = cl.seq_defs()
        expected = {
            '0001': {
                'columns': {
                    0: 'file_id',
                    1: 'file_type',
                    2: 'state',
                    3: 'char_iter',
                    4: 'seq_num',
                    5: 'rec_num',
                    6: 'B00001_001',
                    7: 'B00002_001',
                },
                'tables': {
                    'B00001': {
                        'title': 'UNWEIGHTED SAMPLE COUNT OF THE POPULATION',
                        'subject_area': 'Unweighted Count',
                        'extra': ['Universe:  Total population'],
                        'start_pos': 7,
                        'valtype': 'integer',
                        'items': {
                            'B00001_001': 'Total'
                        }
                    },
                    'B00002': {
                        'title': 'UNWEIGHTED SAMPLE HOUSING UNITS',
                        'subject_area': 'Unweighted Count',
                        'extra': ['Universe:  Housing units'],
                        'start_pos': 8,
                        'valtype': 'integer',
                        'items': {
                            'B00002_001': 'Total'
                        }
                    },
                },
            },
        }
        self.assertEqual(expected, sd)

    def test_seq_defs_many_columns(self):
        tables_ids = {'B01001': {}}
        cl = self.getCensusLoaderForSeq(tables_ids)
        sd = cl.seq_defs()
        expected = {
            '0002': {
                'columns': {
                    0: 'file_id',
                    1: 'file_type',
                    2: 'state',
                    3: 'char_iter',
                    4: 'seq_num',
                    5: 'rec_num',
                    6: 'B01001_001',
                    7: 'B01001_002',
                    8: 'B01001_003',
                    9: 'B01001_004',
                    10: 'B01001_005',
                    11: 'B01001_006',
                    12: 'B01001_007',
                    13: 'B01001_008',
                    14: 'B01001_009',
                    15: 'B01001_010',
                    16: 'B01001_011',
                    17: 'B01001_012',
                    18: 'B01001_013',
                    19: 'B01001_014',
                    20: 'B01001_015',
                    21: 'B01001_016',
                    22: 'B01001_017',
                    23: 'B01001_018',
                    24: 'B01001_019',
                    25: 'B01001_020',
                    26: 'B01001_021',
                    27: 'B01001_022',
                    28: 'B01001_023',
                    29: 'B01001_024',
                    30: 'B01001_025',
                    31: 'B01001_026',
                    32: 'B01001_027',
                    33: 'B01001_028',
                    34: 'B01001_029',
                    35: 'B01001_030',
                    36: 'B01001_031',
                    37: 'B01001_032',
                    38: 'B01001_033',
                    39: 'B01001_034',
                    40: 'B01001_035',
                    41: 'B01001_036',
                    42: 'B01001_037',
                    43: 'B01001_038',
                    44: 'B01001_039',
                    45: 'B01001_040',
                    46: 'B01001_041',
                    47: 'B01001_042',
                    48: 'B01001_043',
                    49: 'B01001_044',
                    50: 'B01001_045',
                    51: 'B01001_046',
                    52: 'B01001_047',
                    53: 'B01001_048',
                    54: 'B01001_049',
                },
                'tables': {
                    'B01001': {
                        'title': 'SEX BY AGE',
                        'subject_area': 'Age-Sex',
                        'extra': ['Universe:  Total population'],
                        'start_pos': 7,
                        'valtype': 'integer',
                        'items': {
                            'B01001_001': 'Total:',
                            'B01001_002': 'Male:',
                            'B01001_003': 'Under 5 years',
                            'B01001_004': '5 to 9 years',
                            'B01001_005': '10 to 14 years',
                            'B01001_006': '15 to 17 years',
                            'B01001_007': '18 and 19 years',
                            'B01001_008': '20 years',
                            'B01001_009': '21 years',
                            'B01001_010': '22 to 24 years',
                            'B01001_011': '25 to 29 years',
                            'B01001_012': '30 to 34 years',
                            'B01001_013': '35 to 39 years',
                            'B01001_014': '40 to 44 years',
                            'B01001_015': '45 to 49 years',
                            'B01001_016': '50 to 54 years',
                            'B01001_017': '55 to 59 years',
                            'B01001_018': '60 and 61 years',
                            'B01001_019': '62 to 64 years',
                            'B01001_020': '65 and 66 years',
                            'B01001_021': '67 to 69 years',
                            'B01001_022': '70 to 74 years',
                            'B01001_023': '75 to 79 years',
                            'B01001_024': '80 to 84 years',
                            'B01001_025': '85 years and over',
                            'B01001_026': 'Female:',
                            'B01001_027': 'Under 5 years',
                            'B01001_028': '5 to 9 years',
                            'B01001_029': '10 to 14 years',
                            'B01001_030': '15 to 17 years',
                            'B01001_031': '18 and 19 years',
                            'B01001_032': '20 years',
                            'B01001_033': '21 years',
                            'B01001_034': '22 to 24 years',
                            'B01001_035': '25 to 29 years',
                            'B01001_036': '30 to 34 years',
                            'B01001_037': '35 to 39 years',
                            'B01001_038': '40 to 44 years',
                            'B01001_039': '45 to 49 years',
                            'B01001_040': '50 to 54 years',
                            'B01001_041': '55 to 59 years',
                            'B01001_042': '60 and 61 years',
                            'B01001_043': '62 to 64 years',
                            'B01001_044': '65 and 66 years',
                            'B01001_045': '67 to 69 years',
                            'B01001_046': '70 to 74 years',
                            'B01001_047': '75 to 79 years',
                            'B01001_048': '80 to 84 years',
                            'B01001_049': '85 years and over'
                        }
                    }
                }
            }
        }
        self.assertEqual(expected, sd)

    def test_to_title_1(self):
        in1 = 'THIS IS A YELLING TITLE'
        expected = 'This is a Yelling Title'
        self.assertEqual(expected, CensusLoader.to_title(in1))

    def test_model_declaration(self):
        table_ids = {
            'B19113': {},
            'B00001': {},
            'B01002': {
                'valtype': 'decimal:5,2',
            },
        }
        cl = self.getCensusLoaderForSeq(table_ids)
        model_decl = cl.model_declaration()
        expected = """\
from django.db import models
from boundaryservice.models import Boundary


class Census(models.Model):
    '''Selected items from U.S. Census 5-Year Summary for Boundary'''

    class Meta:
        verbose_name_plural = "census"

    boundary = models.ForeignKey(Boundary, blank=True, null=True)
    state_abbr = models.CharField(
        max_length=2, help_text='State / U.S. - Abbreviation (USPS)')
    logical_num = models.IntegerField(help_text='Logical record number')

    # B00001 - Unweighted Sample Count of the Population
    B00001_001E = models.IntegerField(
        blank=True, null=True,
        help_text='Unweighted Sample Count of the Population: Total')

    # B01002 - Median Age by Sex
    B01002_001E = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True,
        help_text='Median Age by Sex: Total:')
    B01002_002E = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True,
        help_text='Male')
    B01002_003E = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True,
        help_text='Female')

    # B19113 - Median Family Income In the Past 12 Months (In 2012
    #          Inflation-Adjusted Dollars)
    B19113_001E = models.IntegerField(
        blank=True, null=True,
        help_text=(
            'Median family income in the past 12 months (in 2012'
            ' inflation-adjusted dollars)'))\
"""
        self.assertMultiLineEqual(expected, model_decl)

    def getCensusLoaderForGeo(self, fake_geo):
        self.assertEqual(1269, len(fake_geo))
        cl = CensusLoader([], ['xx'])
        cl.open_geo = mock.MagicMock(name='open_geo')
        cl.open_geo.return_value = StringIO.StringIO(fake_geo)
        cl.add_geo_record = mock.MagicMock(name='add_geo_record')
        cl.add_geo_record.return_value = True
        return cl

    def test_geo_state(self):
        geo = (
            'ACSSF OK040000000001     40                                  '
            '                                                             '
            '                                                        04000'
            'US40                               Oklahoma' + ' '*1042 + '\n')
        cl = self.getCensusLoaderForGeo(geo)
        cl.load_geography_state_domain('OK', cl.GEO_ALL)
        cl.add_geo_record.assert_called_once_with(
            'OK', '0000001', '40', 'states')

    def test_geo_state_wrong_component(self):
        geo = (
            'ACSSF OK040010000002     40                                  '
            '                                                             '
            '                                 U                      04001'
            'US40                               Oklahoma -- Urban' +
            ' '*1033 + '\n')
        cl = self.getCensusLoaderForGeo(geo)
        cl.load_geography_state_domain('OK', cl.GEO_ALL)
        cl.add_geo_record.side_effect = Exception('Not Called')
