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
        return ScoreNode(slug='percent-poverty', metric=metric)

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
