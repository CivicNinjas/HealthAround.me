import json

from boundaryservice.models import Boundary, BoundarySet
from django.test import TestCase as BaseTestCase

from data.models import Census
from healthdata.models import ScoreMetric, ScoreNode
from healthdata.utils import fake_boundary


class TestCase(BaseTestCase):
    maxDiff = None

    def assertScoreEqual(self, expected, calculated):
        '''
        Assert calculated is equal to the equivalent dict

        calculated includes OrderDicts, so it is serialized through
        JSON to turn them into plain dicts
        '''
        actual = json.loads(json.dumps(calculated))
        self.assertDictEqual(expected, actual)


class FakeAlgorithmTest(TestCase):
    def setUp(self):
        self.point = (-95.9907, 36.1524)
        self.boundary = fake_boundary(self.point, 2)

    def assertRandomResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.18,
                u"value": 0.64,
                u"value_type": u"percent",
                u"description": u"A random statistic",
            },
            u"detail": {
                u"path": u"/api/detail/fake_2_-96.00_36.15/random-stat/",
                u"score_text": (
                    u"We don't have data for Random Stat yet, but studies show"
                    u" it has an impact on the health of a community. Do you"
                    u" know about a data source?"
                    u" <a href='#'>Tell us about it</a>."),
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_-96.00_36.15/",
                u"label": "Future Data Placeholder",
                u"type": "Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def random_stat_node(self):
        metric = ScoreMetric.objects.create(
            name=u"Random Stat",
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM,
            description=u"A random statistic")
        return ScoreNode(
            slug='random-stat', metric=metric, label='Random Stat')

    def test_calculate_random_stat_by_boundary(self):
        node = self.random_stat_node()
        calculated = node.score_by_boundary(self.boundary)
        self.assertRandomResult(calculated)

    def test_calculate_random_stat_by_location(self):
        node = self.random_stat_node()
        location = (-95.994, 36.153)
        score = node.score_by_location(location)
        self.assertRandomResult(score)

    def test_score_other_random_stat_by_boundary(self):
        metric = ScoreMetric.objects.create(
            name=u"Other Random Stat",
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM,
            description=u"Another random statistic")
        node = ScoreNode(
            slug='other-stat', metric=metric, label='Other Stat')
        score = node.score_by_boundary(self.boundary)
        expected = {
            u"summary": {
                u"score": 0.03,
                u"value": 0.76,
                u"value_type": u"percent",
                u"description": u"Another random statistic",
            },
            u"detail": {
                u"path": (
                    u"/api/detail/fake_2_-96.00_36.15/other-stat/"),
                u"score_text": (
                    u"We don't have data for Other Stat yet, but studies show"
                    u" it has an impact on the health of a community. Do you"
                    u" know about a data source?"
                    u" <a href='#'>Tell us about it</a>."),
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_-96.00_36.15/",
                u"label": "Future Data Placeholder",
                u"type": "Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)


class PercentAlgorithmTest(TestCase):
    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='Census Tract',
            slug='census-tracts',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
        shape = (
            'MULTIPOLYGON ((('
            '-96.00269 36.14836, -96.00269 36.15019, -96.00154 36.15488, '
            '-96.00169 36.15608, -96.00138 36.15608, -96.00149 36.15648, '
            '-96.00091 36.15798, -96.00060 36.15807, -95.99898 36.16035, '
            '-95.99903 36.16052, -95.99776 36.16078, -95.99788 36.16099, '
            '-95.99532 36.16147, -95.99286 36.16221, -95.99030 36.16237, '
            '-95.98693 36.16103, -95.98393 36.16057, -95.98096 36.15979, '
            '-95.98068 36.15918, -95.98038 36.15274, -95.98059 36.14949, '
            '-95.97970 36.14593, -95.98005 36.14427, -95.98061 36.14340, '
            '-95.98136 36.14282, -95.98243 36.14243, -95.98381 36.14245, '
            '-95.98732 36.14377, -95.99231 36.14423, -95.99455 36.14526, '
            '-95.99611 36.14555, -95.99969 36.14541, -96.00045 36.14555, '
            '-96.00182 36.14595, -96.00224 36.14639, -96.00260 36.14702, '
            '-96.00269 36.14836)))')
        self.tract = Boundary.objects.create(
            slug='census-tract-25',
            name='Census Tract 25',
            set=self.tract_set,
            metadata={'GEOID': '40143002500'},
            external_id='40143002500',
            shape=shape,
            display_name='Census Tract 25',
            kind='Census Tract',
            simple_shape=shape)
        self.location = (-95.99, 36.15)
        Census.objects.create(
            boundary=self.tract,
            logical_num=4846,
            B19058_001E=1042,
            B19058_002E=217,
            B19058_003E=825,
            B17001_001E=1643,
            B17001_002E=534,
            B23001_001E=3186,
            B23001_008E=0.00,
            B23001_015E=0.00,
            B23001_022E=0.00,
            B23001_029E=0.00,
            B23001_036E=23.0,
            B23001_043E=40.0,
            B23001_050E=23.0,
            B23001_057E=22.0,
            B23001_064E=0.00,
            B23001_071E=0.00,
            B23001_076E=0.00,
            B23001_081E=10.0,
            B23001_086E=0.00,
            B23001_094E=0.00,
            B23001_101E=0.00,
            B23001_108E=0.00,
            B23001_115E=0.00,
            B23001_122E=8.00,
            B23001_129E=5.00,
            B23001_136E=0.00,
            B23001_143E=0.00,
            B23001_150E=0.00,
            B23001_157E=0.00,
            B23001_162E=0.00,
            B23001_167E=0.00,
            B23001_172E=0.00,
            B09002_001E=4.00,
            B09002_008E=0.00,
            B25091_001E=147.0,
            B25070_001E=895.0,
            B25070_008E=52.0,
            B25070_009E=54.0,
            B25070_010E=215.0,
            B25091_009E=0.00,
            B25091_010E=4.00,
            B25091_011E=11.0,
            B25091_020E=0.00,
            B25091_021E=0.00,
            B25091_022E=0.00,
            B15002_001E=2616.0,
            B15002_011E=624.0,
            B15002_012E=130.0,
            B15002_013E=254.0,
            B15002_014E=54.0,
            B15002_015E=229.0,
            B15002_016E=64.0,
            B15002_017E=21.0,
            B15002_018E=6.0,
            B15002_028E=179.0,
            B15002_029E=40.0,
            B15002_030E=68.0,
            B15002_031E=41.0,
            B15002_032E=185.0,
            B15002_033E=53.0,
            B15002_034E=13.0,
            B15002_035E=15.0,
            B12001_001E=3191,
            B12001_003E=1354,
            B12001_009E=19,
            B12001_012E=374,
            B12001_018E=66,
            B12001_005E=137,
            B12001_014E=145,
            B25014_001E=1042,
            B25014_003E=127,
            B25014_004E=20,
            B25014_005E=0,
            B25014_006E=0,
            B25014_007E=0,
            B25014_009E=645,
            B25014_010E=231,
            B25014_011E=0,
            B25014_012E=19,
            B25014_013E=0,
            B07013_001E=1404,
            B07013_004E=788,
            B15003_001E=2616,
            B15003_021E=95,
            B15003_022E=414,
            B15003_023E=117,
            B15003_024E=34,
            B15003_025E=21,
            B08303_001E=941,
            B08303_008E=20,
            B08303_009E=10,
            B08303_010E=13,
            B08303_011E=12,
            B08303_012E=68,
            B08303_013E=0,
            B25052_001E=1042,
            B25052_003E=7,
            B25048_001E=1042,
            B25048_003E=0,
            B25075_001E=147,
            B25075_002E=0,
            B25075_003E=0,
            B25075_004E=0,
            B25075_005E=0,
            B25075_006E=0,
            B25075_007E=0,
            B25075_008E=0,
            B25075_009E=19,
            B25075_010E=4,
            B25075_011E=9,
            B25075_012E=44,
            B25075_013E=6,
            B25075_014E=27,
            B25075_015E=12,
        )

    def food_stamp_node(self):
        metric = ScoreMetric.objects.create(
            name="% Food Stamp",
            algorithm=ScoreMetric.FOOD_STAMP_ALGORITHM,
            description=(
                "% of households on public assistance income or food"
                " stamps/SNAP in the past 12 months")
        )
        return ScoreNode(slug='food-stamp', metric=metric)

    def assertFoodStampResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.254,
                u"value": 0.208,
                u"average": 0.138,
                u"std_dev": 0.106,
                u"value_type": u"percent",
                u"description": (
                    u"% of households on public assistance income or food"
                    u" stamps/SNAP in the past 12 months"),
            },
            u'detail': {
                u"path": u"/api/detail/census-tract-25/food-stamp/",
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_food_stamp_by_boundary(self):
        node = self.food_stamp_node()
        score = node.score_by_boundary(self.tract)
        self.assertFoodStampResult(score)

    def test_food_stamp_by_location(self):
        node = self.food_stamp_node()
        score = node.score_by_location(self.location)
        self.assertFoodStampResult(score)

    def percent_poverty_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Poverty",
            algorithm=ScoreMetric.PERCENT_POVERTY_ALGORITHM,
            description=(
                "Percent Poverty status in the past 12 months")
        )
        return ScoreNode(
            slug='percent-poverty', metric=metric, label='Percent Poverty')

    def assertPercentPovertyResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.09,
                u"value": 0.325,
                u"average": 0.166,
                u"std_dev": 0.118383,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-poverty/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_poverty_by_boundary(self):
        node = self.percent_poverty_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentPovertyResult(score)

    def test_percent_poverty_by_location(self):
        node = self.percent_poverty_node()
        score = node.score_by_location(self.location)
        self.assertPercentPovertyResult(score)

    def test_by_location_skips_null_boundary(self):
        block_group_set = BoundarySet.objects.create(
            name='Census Block Groups',
            slug='census-block-groups',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])
        shape = (
            'MULTIPOLYGON ((('
            '-96.00269 36.14836, -96.00217 36.14869, -96.00213 36.14798, '
            '-95.99806 36.14791, -95.99935 36.15051, -95.99702 36.15139, '
            '-95.99649 36.15038, -95.98948 36.15279, -95.98841 36.15086, '
            '-95.98952 36.15050, -95.98733 36.14637, -95.98732 36.14377, '
            '-95.99231 36.14423, -95.99455 36.14527, -95.99611 36.14555, '
            '-95.99969 36.14541, -96.00182 36.14595, -96.00260 36.14702, '
            '-96.00269 36.14836)))')
        block_group = Boundary.objects.create(
            slug='census-block-group-002500-1',
            name='002500 1',
            set=block_group_set,
            metadata={'GEOID': '40143002500'},
            external_id='401430025001',
            shape=shape,
            display_name='Census Block Group 002500 1',
            kind='Census Block Group',
            simple_shape=shape)
        Census.objects.create(
            boundary=block_group,
            logical_num=7506,
            B17001_001E=None,
            B17001_002E=None)
        node = self.percent_poverty_node()
        score = node.score_by_location(self.location)
        self.assertPercentPovertyResult(score)

    def test_by_location_no_boundary_is_placeholder(self):
        node = self.percent_poverty_node()
        score = node.score_by_location((0, 0))
        expected = {
            u"summary": {
                u"score": 0.66,
                u"value": 0.41,
                u"value_type": u"percent",
                u"description": (
                    u"Percent Poverty status in the past 12 months"),
            },
            u"detail": {
                u"path": u"/api/detail/fake_2_0.00_0.00/percent-poverty/",
                u"score_text": (
                    u"We don't have data for Percent Poverty yet, but studies"
                    u" show it has an impact on the health of a community. Do"
                    u" you know about a data source?"
                    u" <a href='#'>Tell us about it</a>."),
            },
            u"boundary": {
                u"path": u"/api/boundary/fake_2_0.00_0.00/",
                u"label": u"Future Data Placeholder",
                u"type": u"Placeholder",
            },
        }
        self.assertScoreEqual(expected, score)

    def percent_employment_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Unemployment",
            algorithm=ScoreMetric.PERCENT_UNEMPLOYMENT_ALGORITHM,
            description="Percent Unemployment in the past 12 months",
        )
        return ScoreNode(slug='percent-employment', metric=metric)

    def assertPercentEmploymentResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.512,
                u"value": 0.041,
                u"average": 0.04193,
                u"std_dev": 0.0266,
                u"value_type": "percent",
                u"description": "Percent Unemployment in the past 12 months",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-employment/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_employment_by_boundary(self):
        node = self.percent_employment_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentEmploymentResult(score)

    def test_percent_employment_by_location(self):
        node = self.percent_employment_node()
        score = node.score_by_location(self.location)
        self.assertPercentEmploymentResult(score)

    def percent_single_parent_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Single Parent",
            algorithm=ScoreMetric.PERCENT_SINGLE_PARENT_ALGORITHM,
            description="Percent of Children Living with a Single Parent",
        )
        return ScoreNode(slug='percent-single-parent', metric=metric)

    def assertPercentSingleParentResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.997,
                u"value": 0.0,
                u"average": 0.452998,
                u"std_dev": 0.1657150,
                u"value_type": u"percent",
                u"description": (
                    u"Percent of Children Living with a Single Parent")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-single-parent/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_single_parent_by_boundary(self):
        node = self.percent_single_parent_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentSingleParentResult(score)

    def test_percent_single_parent_by_location(self):
        node = self.percent_single_parent_node()
        score = node.score_by_location(self.location)
        self.assertPercentSingleParentResult(score)

    def percent_income_housing_cost_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Income Housing Cost",
            algorithm=ScoreMetric.PERCENT_INCOME_HOUSING_COST_ALGORITHM,
            description=(
                "Data calculated from values in both of these tables."),
        )
        return ScoreNode(
            slug='percent-income-housing-cost-node', metric=metric)

    def assertPercentIncomeHousingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.118,
                u"value": 0.257,
                u"average": 0.1544959,
                u"std_dev": 0.0867039,
                u"value_type": u"percent",
                u"description": (
                    u"Data calculated from values in both of these tables."),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-income-housing-cost-node/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_income_housing_cost_by_boundary(self):
        node = self.percent_income_housing_cost_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentIncomeHousingResult(score)

    def test_percent_income_housing_cost_by_location(self):
        node = self.percent_income_housing_cost_node()
        score = node.score_by_location(self.location)
        self.assertPercentIncomeHousingResult(score)

    def percent_high_school_graduates_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent High School Graduates",
            algorithm=ScoreMetric.PERCENT_HIGH_SCHOOL_GRADUATES_ALGORITHM,
            description=(
                "Educational Attainment for the Population 25 Years and Over")
        )
        return ScoreNode(
            slug='percent-high-school-graduates', metric=metric)

    def assertPercentHighSchoolGraduatesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.136,
                u"value": 0.755,
                u"average": 0.861836,
                u"std_dev": 0.096739,
                u"value_type": u"percent",
                u"description": (
                    u"Educational Attainment for the Population"
                    u" 25 Years and Over"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-high-school-graduates/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_high_school_graduates_by_boundary(self):
        node = self.percent_high_school_graduates_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentHighSchoolGraduatesResult(score)

    def test_percent_high_school_graduates_by_location(self):
        node = self.percent_high_school_graduates_node()
        score = node.score_by_location(self.location)
        self.assertPercentHighSchoolGraduatesResult(score)

    def percent_divorced_or_separated_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Divorced or Separated",
            algorithm=ScoreMetric.PERCENT_DIVORCED_ALGORITHM,
            description=(
                "Percent of Population Divorced or Separated"
                " 15 Years and Over")
        )
        return ScoreNode(slug='percent-divorced-married', metric=metric)

    def assertPercentDivorcedOrSeparatedResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.0,
                u"value": 0.795,
                u"average": 0.264508,
                u"std_dev": 0.139789,
                u"value_type": u"percent",
                u"description": (
                    "Percent of Population Divorced or Separated"
                    " 15 Years and Over")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-divorced-married/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_divorced_or_separated_by_boundary(self):
        node = self.percent_divorced_or_separated_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentDivorcedOrSeparatedResult(score)

    def test_percent_divorced_or_separated_by_location(self):
        node = self.percent_divorced_or_separated_node()
        score = node.score_by_location(self.location)
        self.assertPercentDivorcedOrSeparatedResult(score)

    def percent_overcrowded_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Overcrowding in Residences",
            algorithm=ScoreMetric.PERCENT_OVERCROWDING_ALGORITHM,
            description="Tenure by Occupants per Room",
        )
        return ScoreNode(slug='percent-overcrowded', metric=metric)

    def assertPercentOvercrowdedResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.536,
                u"value": 0.039,
                u"average": 0.040577,
                u"std_dev": 0.014887,
                u"value_type": u"percent",
                u"description": "Tenure by Occupants per Room",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-overcrowded/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_overcrowded_by_boundary(self):
        node = self.percent_overcrowded_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentOvercrowdedResult(score)

    def test_percent_overcrowded_by_location(self):
        node = self.percent_overcrowded_node()
        score = node.score_by_location(self.location)
        self.assertPercentOvercrowdedResult(score)

    def percent_geographic_mobility_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Geographic Movement in a Year",
            algorithm=ScoreMetric.PERCENT_GEOGRAPHIC_MOBILITY_ALGORITHM,
            description=(
                "Geographic Mobility in the Past Year by Tenure for Current"
                " Residence in the United States")
        )
        return ScoreNode(slug='percent-geographic-mobility', metric=metric)

    def assertPercentGeographicMobilityResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.002,
                u"value": 0.439,
                u"average": 0.168965,
                u"std_dev": 0.09219,
                u"value_type": u"percent",
                u"description": (
                    "Geographic Mobility in the Past Year by Tenure for"
                    " Current Residence in the United States"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/"
                    u"percent-geographic-mobility/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_geographic_mobility_by_boundary(self):
        node = self.percent_geographic_mobility_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentGeographicMobilityResult(score)

    def test_percent_geographic_mobility_by_location(self):
        node = self.percent_geographic_mobility_node()
        score = node.score_by_location(self.location)
        self.assertPercentGeographicMobilityResult(score)

    def percent_college_graduates_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent College Graduates",
            algorithm=ScoreMetric.PERCENT_COLLEGE_GRADUATE_ALGORITHM,
            description=(
                "Educational Attainment for the Population 25 Years and Over")
        )
        return ScoreNode(slug='percent-college-graduate', metric=metric)

    def assertPercentCollegeGraduateResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.394,
                u"value": 0.26,
                u"average": 0.301417,
                u"std_dev": 0.153007,
                u"value_type": u"percent",
                u"description": (
                    u"Educational Attainment for the Population"
                    u" 25 Years and Over")
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-college-graduate/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_college_graduate_by_boundary(self):
        node = self.percent_college_graduates_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentCollegeGraduateResult(score)

    def test_percent_college_graduate_by_location(self):
        node = self.percent_college_graduates_node()
        score = node.score_by_location(self.location)
        self.assertPercentCollegeGraduateResult(score)

    def percent_bad_commute_times_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Bad Commute Times",
            algorithm=ScoreMetric.PERCENT_BAD_COMMUTE_TIMES_ALGORITHM,
            description="Travel Time to Work",
        )
        return ScoreNode(slug='percent-bad-commute-times', metric=metric)

    def assertPercentBadCommuteTimesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.488,
                u"value": 0.085,
                u"average": 0.082964,
                u"std_dev": 0.059340889,
                u"value_type": u"percent",
                u"description": u"Travel Time to Work",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-bad-commute-times/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_bad_commute_times_by_boundary(self):
        node = self.percent_bad_commute_times_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentBadCommuteTimesResult(score)

    def test_percent_bad_commute_times_by_location(self):
        node = self.percent_bad_commute_times_node()
        score = node.score_by_location(self.location)
        self.assertPercentBadCommuteTimesResult(score)

    def percent_improper_kitchen_facilities_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Improper Kitchen Facilities",
            algorithm=(
                ScoreMetric.PERCENT_IMPROPER_KITCHEN_FACILITIES_ALGORITHM),
            description="Kitchen Facilities for Occupied Housing Units",
        )
        return ScoreNode(
            slug='percent-improper-kitchen-facilities', metric=metric)

    def assertPercentImproperKitchenFacilitiesResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.567,
                u"value": 0.007,
                u"average": 0.00976313,
                u"std_dev": 0.01802429,
                u"value_type": u"percent",
                u"description": (
                    u"Kitchen Facilities for Occupied Housing Units"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25"
                    u"/percent-improper-kitchen-facilities/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_improper_kitchen_facilities_by_boundary(self):
        node = self.percent_improper_kitchen_facilities_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentImproperKitchenFacilitiesResult(score)

    def test_percent_improper_kitchen_facilities_by_location(self):
        node = self.percent_improper_kitchen_facilities_node()
        score = node.score_by_location(self.location)
        self.assertPercentImproperKitchenFacilitiesResult(score)

    def percent_improper_plumbing_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Improper Plumbing",
            algorithm=ScoreMetric.PERCENT_IMPROPER_PLUMBING_ALGORITHM,
            description="Plumbing Facilities for Occupied Housing Units",
        )
        return ScoreNode(slug='percent-improper-plumbing', metric=metric)

    def assertPercentImproperPlumbingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.7,
                u"value": 0.0,
                u"average": 0.00572503,
                u"std_dev": 0.0109313,
                u"value_type": u"percent",
                u"description": (
                    u"Plumbing Facilities for Occupied Housing Units"),
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-improper-plumbing/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_improper_plumbing_by_boundary(self):
        node = self.percent_improper_plumbing_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentImproperPlumbingResult(score)

    def test_percent_improper_plumbing_by_location(self):
        node = self.percent_improper_plumbing_node()
        score = node.score_by_location(self.location)
        self.assertPercentImproperPlumbingResult(score)

    def percent_low_value_housing_node(self):
        metric = ScoreMetric.objects.create(
            name="Percent Low Value Housing",
            algorithm=ScoreMetric.PERCENT_LOW_VALUE_HOUSING_ALGORITHM,
            description="Value",
        )
        return ScoreNode(slug='percent-low-value-housing', metric=metric)

    def assertPercentLowValueHousingResult(self, score):
        expected = {
            u"summary": {
                u"score": 0.755,
                u"value": 0.018,
                u"average": 0.0575880,
                u"std_dev": 0.057490381,
                u"value_type": u"percent",
                u"description": u"Value",
            },
            u'detail': {
                u"path": (
                    u"/api/detail/census-tract-25/percent-low-value-housing/"),
            },
            u"boundary": {
                u"path": u"/api/boundary/census-tract-25/",
                u"label": u"Census Tract 25",
                u"type": u"Census Tract",
                u"external_id": u'40143002500',
            }
        }
        self.assertScoreEqual(expected, score)

    def test_percent_low_value_housing_by_boundary(self):
        node = self.percent_low_value_housing_node()
        score = node.score_by_boundary(self.tract)
        self.assertPercentLowValueHousingResult(score)

    def test_percent_low_value_housing_by_location(self):
        node = self.percent_low_value_housing_node()
        score = node.score_by_location(self.location)
        self.assertPercentLowValueHousingResult(score)
