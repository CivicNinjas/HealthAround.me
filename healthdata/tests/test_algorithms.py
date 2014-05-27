from boundaryservice.models import Boundary, BoundarySet
from django.test import TestCase

from data.models import Census
from healthdata.models import ScoreMetric


class FakeAlgorithmTest(TestCase):
    maxDiff = None

    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='Census Tract',
            kind_first=True,
            last_updated='2014-05-21',
            count=0,
            metadata_fields=['GEOID'])

    def assertBoundary(self, slug, point_id, boundary):
        expected_boundary = {
            "path": '/api/boundary/fake/{}/{}/'.format(slug, point_id),
            'label': u'Fake Data Boundary',
            'year': 2010,
            'type': 'fake',
            'id': point_id,
        }
        self.assertEqual(expected_boundary, dict(boundary))

    def assertCitation(self, slug, point_id, citation):
        expected_citation = {
            'path': '/api/citation/fake/{}/{}/'.format(slug, point_id),
            'label': 'Fake Data Citation',
            'year': 2010,
            'type': 'fake',
            'id': point_id,
        }
        self.assertEqual(expected_citation, dict(citation))

    def test_calculate_random_stat(self):
        metric = ScoreMetric.objects.create(
            name=u"Random Stat",
            algorithm=ScoreMetric.FAKE_ALGORITHM,
            boundary_set=self.tract_set,
            description=u"A random statistic")
        point = (-95.9907, 36.1524)
        point_id = '-95.9907,36.1524'
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_score = {
            "score": 0.36,
            "value": 0.17,
            "value_type": "percent",
            "description": u"A random statistic",
            "citation_path": (
                '/api/citation/fake/random-stat/{}/'.format(point_id)),
            "boundary_path": (
                '/api/boundary/fake/random-stat/{}/'.format(point_id)),
        }
        self.assertEqual(expected_score, dict(score))
        self.assertCitation('random-stat', point_id, citation)
        self.assertBoundary('random-stat', point_id, boundary)

    def test_calculate_other_random_stat(self):
        metric = ScoreMetric.objects.create(
            name=u"Other Random Stat",
            algorithm=ScoreMetric.FAKE_ALGORITHM,
            boundary_set=self.tract_set,
            description=u"Another random statistic")
        point = (-95.9907, 36.1524)
        point_id = '-95.9907,36.1524'
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_score = {
            "score": 0.36,
            "value": 0.47,
            "value_type": "percent",
            "description": u"Another random statistic",
            "citation_path": (
                '/api/citation/fake/other-random-stat/{}/'.format(point_id)),
            "boundary_path": (
                '/api/boundary/fake/other-random-stat/{}/'.format(point_id)),
        }
        self.assertEqual(expected_score, dict(score))
        self.assertCitation('other-random-stat', point_id, citation)
        self.assertBoundary('other-random-stat', point_id, boundary)


class PercentAlgorithmTest(TestCase):
    maxDiff = None

    def setUp(self):
        self.tract_set = BoundarySet.objects.create(
            name='Census Tract',
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
        tract = Boundary.objects.create(
            slug='census-tract-25',
            set=self.tract_set,
            metadata={'GEOID': '40143002500'},
            external_id='40143002500',
            shape=shape,
            display_name='Census Tract 25',
            simple_shape=shape)
        Census.objects.create(
            boundary=tract,
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
        )

    def assertBoundary(self, boundary):
        expected_boundary = {
            'path': '/api/boundary/census-tract-25/',
            'label': u'Census Tract 25',
            'year': 2013,
            'external_id': u'40143002500',
            'type': u'Census Tract',
            'id': u'census-tract-25',
        }
        self.assertEqual(expected_boundary, dict(boundary))

    def assertCitation(self, citation_id, citation):
        expected_citation = {
            'path': '/api/citation/census/{}/'.format(citation_id),
            'label': 'Census 5 Year Summary, 2008-2012',
            'year': 2012,
            'type': 'percent',
            'id': citation_id,
        }
        self.assertEqual(expected_citation, dict(citation))

    def test_food_stamp(self):
        metric = ScoreMetric.objects.create(
            name="% Food Stamp",
            algorithm=ScoreMetric.FOOD_STAMP_ALGORITHM,
            boundary_set=self.tract_set,
            data_property='B19058_001E',
            description=(
                "% of households on public assistance income or food"
                " stamps/SNAP in the past 12 months")
        )
        point = (-95.9907, 36.1524)
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_score = {
            "score": 0.254,
            "value": 0.208,
            "average": 0.138,
            "std_dev": 0.106,
            "value_type": "percent",
            "description": (
                "% of households on public assistance income or food"
                " stamps/SNAP in the past 12 months"),
            "citation_path": '/api/citation/census/B19058/',
            "boundary_path": '/api/boundary/census-tract-25/',
        }
        self.assertEqual(expected_score, dict(score))
        self.assertCitation('B19058', citation)
        self.assertBoundary(boundary)

    def test_percent_poverty(self):
        metric = ScoreMetric.objects.create(
            name="Percent Poverty",
            algorithm=ScoreMetric.PERCENT_POVERTY_ALGORITHM,
            boundary_set=self.tract_set,
            data_property='B17001_001E',
            description=(
                "Percent Poverty status in the past 12 months")
        )
        point = (-95.9907, 36.1524)
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_score = {
            "score": 0.09,
            "value": 0.325,
            "average": 0.166,
            "std_dev": 0.118383,
            "value_type": "percent",
            "description": (
                "Percent Poverty status in the past 12 months"),
            "citation_path": '/api/citation/census/B17001/',
            "boundary_path": '/api/boundary/census-tract-25/',
        }
        self.assertEqual(expected_score, dict(score))
        self.assertCitation('B17001', citation)
        self.assertBoundary(boundary)


    def test_percent_employment(self):
        metric = ScoreMetric.objects.create(
            name = "Percent Unemployment",
            algorithm = ScoreMetric.PERCENT_UNEMPLOYMENT_ALGORITHM,
            boundary_set=self.tract_set,
            data_property = 'B23001_001E',
            description=(
                "Percent Unemployment in the past 12 months")
            )
        point = (-95.9907, 36.1524)
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_score = {
            "score": 0.512,
            "value": 0.041,
            "average": 0.04193,
            "std_dev": 0.0266,
            "value_type": "percent",
            "description": (
                "Percent Unemployment in the past 12 months"),
            "citation_path": '/api/citation/census/B23001/',
            "boundary_path": '/api/boundary/census-tract-25/',           
        }
        self.assertEqual(expected_score, dict(score))
        self.assertCitation('B23001', citation)
        self.assertBoundary(boundary)

