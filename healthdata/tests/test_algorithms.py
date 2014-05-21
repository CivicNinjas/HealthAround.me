from collections import OrderedDict

from boundaryservice.models import Boundary, BoundarySet
from django.test import TestCase

from data.models import Census
from healthdata.models import ScoreMetric


class FoodStampAlgorithmTest(TestCase):
    maxDiff = None

    def test_calculation(self):
        tract_set = BoundarySet.objects.create(
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
            set=tract_set,
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
        )
        metric = ScoreMetric.objects.create(
            name="% Food Stamp",
            algorithm=ScoreMetric.FOOD_STAMP_ALGORITHM,
            boundary_set=tract_set,
            data_property='B19058_001E',
            description=(
                "% of households on public assistance income or food"
                " stamps/SNAP in the past 12 months")
        )
        point = (-95.9907, 36.1524)
        algorithm = metric.get_algorithm()
        score, citation, boundary = algorithm.calculate(point)
        expected_citation = {
            'path': '/api/citation/census/B19058/',
            'label': 'Census 5 Year Summary, 2008-2012',
            'year': 2012,
            'type': 'percent',
            'id': 'B19058',
        }
        expected_boundary = {
            'path': '/api/boundary/census-tract-25/',
            'label': u'Census Tract 25',
            'year': 2013,
            'external_id': u'40143002500',
            'type': u'Census Tract',
            'id': u'census-tract-25',
        }
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
        self.assertEqual(expected_citation, dict(citation))
        self.assertEqual(expected_boundary, dict(boundary))
