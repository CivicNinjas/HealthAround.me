import json

from rest_framework.test import APITestCase as BaseAPITestCase

from healthdata.models import ScoreNode, ScoreMetric


class APITestCase(BaseAPITestCase):
    maxDiff = None

    def assertDataEqual(self, response, expected):
        '''
        assert Response data is equal to a dictionary

        Because data includes dict-like objects that aren't quite dicts, it
        passed through json encoding/decoding first, to get a plain old dict
        (with unicode strings)
        '''
        self.assertEqual(response.status_code, 200, response.content)
        actual = response.data
        data = json.loads(json.dumps(actual))
        self.assertEqual(expected, data)


class DetailAPIViewTest(APITestCase):

    def setUp(self):
        self.metric_a = ScoreMetric.objects.create(
            name=u'Metric A', description=u'The first metric',
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM, params={})
        self.node_a = ScoreNode.objects.create(
            slug='metric-a', label='Metric A', metric=self.metric_a, weight=2)
        self.url = (
            '/api/detail/fake_4_-95.9910_36.1499/metric-a/')

    def test_get(self):
        response = self.client.get(self.url)
        expected = {
            u'id': u'fake_4_-95.9910_36.1499',
            u'type': u'Feature',
            u'geometry': {
                u'type': u'MultiPolygon',
                u'coordinates': [[[
                    [-95.991, 36.1499],
                    [-95.991, 36.15],
                    [-95.9909, 36.15],
                    [-95.9909, 36.1499],
                    [-95.991, 36.1499],
                ]]]},
            u'properties': {
                u'name': u'Placeholder',
                u'display_name': u'Future Data Placeholder',
                u'external_id': u'',
                u'kind': u'Future Data Placeholder',
                u'centroid': {
                    u'type': u'Point',
                    u'coordinates': [-95.99095, 36.14995],
                },
                u'metric': {
                    u'label': u'Metric A',
                    u'slug': u'metric-a',
                    u'description': u'The first metric',
                    u'weight': 2,
                    u'score': 0.53,
                    u'score_text': (
                        u"We don't have data for Metric A yet, but studies"
                        u" show it has an impact on the health of a"
                        u" community. Do you know about a data source?"
                        u" <a href='#'>Tell us about it</a>."
                    ),
                    u'value': 0.46,
                    u'value_type': u'percent',
                },
            }
        }
        self.assertDataEqual(response, expected)


class FakeBoundaryAPIView(APITestCase):
    def test_get(self):
        url = '/api/boundary/fake_2_-95.99_36.15/'
        response = self.client.get(url)
        expected = {
            u'geometry': {
                u'coordinates': [[[
                    [-95.99, 36.15],
                    [-95.99, 36.16],
                    [-95.98, 36.16],
                    [-95.98, 36.15],
                    [-95.99, 36.15]]]],
                u'type': u'MultiPolygon'},
            u'type': u'Feature',
            u'id': u'fake_2_-95.99_36.15',
            u'properties': {
                u'centroid': {
                    u'coordinates': [-95.985, 36.155],
                    u'type': u'Point'},
                u'display_name': u'Future Data Placeholder',
                u'external_id': u'',
                u'kind': u'Future Data Placeholder',
                u'name': u'Placeholder'}}
        self.assertDataEqual(response, expected)


class ScoreAPIViewTest(APITestCase):

    def setUp(self):
        self.parent_node = ScoreNode.objects.create(
            slug='parent', label='Parent', weight=1)
        self.metric_a = ScoreMetric.objects.create(
            name=u'Metric A', description=u'The first metric',
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM, params={})
        self.node_a = ScoreNode.objects.create(
            slug='metric-a', label='Metric A', metric=self.metric_a, weight=2,
            parent=self.parent_node)
        self.metric_b = ScoreMetric.objects.create(
            name=u'Metric B', description=u'The second metric',
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM, params={})
        self.node_b = ScoreNode.objects.create(
            slug='metric-b', label='Metric B', metric=self.metric_b, weight=1,
            parent=self.parent_node)
        self.url = '/api/score/-95.991,36.1499/'

    def test_get(self):
        response = self.client.get(self.url)
        expected = {
            u'elements': [{
                u'label': u'Parent',
                u'slug': u'parent',
                u'weight': 1,
                u'score': 0.5,
                u'elements': [{
                    u'label': u'Metric A',
                    u'slug': u'metric-a',
                    u'description': u'The first metric',
                    u'weight': 2,
                    u'score': 0.35,
                    u'value': 0.2,
                    u'value_type': u'percent',
                    u'boundary_id': u'fake_2_-96.00_36.14',
                    u'detail_uri': (
                        u'http://testserver'
                        u'/api/detail/fake_2_-96.00_36.14/metric-a/'),
                }, {
                    u'label': u'Metric B',
                    u'slug': u'metric-b',
                    u'description': u'The second metric',
                    u'weight': 1,
                    u'score': 0.8,
                    u'value': 0.87,
                    u'value_type': u'percent',
                    u'boundary_id': u'fake_2_-96.00_36.14',
                    u'detail_uri': (
                        u'http://testserver'
                        u'/api/detail/fake_2_-96.00_36.14/metric-b/'),
                }],
            }],
            u'boundaries': {
                u'fake_2_-96.00_36.14': {
                    u'path': u'/api/boundary/fake_2_-96.00_36.14/',
                    u'uri': (
                        u'http://testserver'
                        u'/api/boundary/fake_2_-96.00_36.14/'),
                    u'type': u'Placeholder',
                    u'label': u'Future Data Placeholder',
                },
            },
        }
        self.assertDataEqual(response, expected)
