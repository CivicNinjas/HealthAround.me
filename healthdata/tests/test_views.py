import json

from rest_framework.test import APITestCase

from healthdata.models import ScoreNode, ScoreMetric


class ScoreAPIViewTest(APITestCase):
    maxDiff = None

    def setUp(self):
        self.parent_node = ScoreNode.objects.create(
            slug='parent', label='Parent', weight=1)
        self.metric_a = ScoreMetric.objects.create(
            name=u'Metric A', description=u'The first metric',
            algorithm=ScoreMetric.FAKE_ALGORITHM, params={})
        self.node_a = ScoreNode.objects.create(
            slug='metric-a', label='Metric A', metric=self.metric_a, weight=2,
            parent=self.parent_node)
        self.metric_b = ScoreMetric.objects.create(
            name=u'Metric B', description=u'The second metric',
            algorithm=ScoreMetric.FAKE_ALGORITHM, params={})
        self.node_b = ScoreNode.objects.create(
            slug='metric-b', label='Metric B', metric=self.metric_b, weight=1,
            parent=self.parent_node)
        self.url = '/api/score/-95.991,36.1499/'

    def assertResponseDataEqual(self, expected, actual):
        '''
        assert Response data is equal to a dictionary

        Because data includes dict-like objects that aren't quite dicts, it
        passed through json encoding/decoding first, to get a plain old dict
        (with unicode strings)
        '''
        data = json.loads(json.dumps(actual))
        self.assertEqual(expected, data)

    def test_get(self):
        response = self.client.get(self.url)
        expected = {
            u'elements': [{
                u'label': u'Parent',
                u'slug': u'parent',
                u'weight': 1,
                u'score': 0.75,
                u'elements': [{
                    u'label': u'Metric A',
                    u'slug': u'metric-a',
                    u'description': u'The first metric',
                    u'weight': 2,
                    u'score': 0.73,
                    u'value': 0.61,
                    u'value_type': u'percent',
                    u'citation_path': (
                        u'/api/citation/fake/metric-a/-95.9910,36.1499/'),
                    u'boundary_path': (
                        u'/api/boundary/fake/metric-a/-95.9910,36.1499/'),
                }, {
                    u'label': u'Metric B',
                    u'slug': u'metric-b',
                    u'description': u'The second metric',
                    u'weight': 1,
                    u'score': 0.78,
                    u'value': 0.2,
                    u'value_type': u'percent',
                    u'citation_path': (
                        u'/api/citation/fake/metric-b/-95.9910,36.1499/'),
                    u'boundary_path': (
                        u'/api/boundary/fake/metric-b/-95.9910,36.1499/'),
                }],
            }],
            u'citations': {
                u'/api/citation/fake/metric-a/-95.9910,36.1499/': {
                    u'path': u'/api/citation/fake/metric-a/-95.9910,36.1499/',
                    u'id': u'-95.9910,36.1499',
                    u'year': 2010,
                    u'type': u'fake',
                    u'label': u'Fake Data Citation',
                },
                u'/api/citation/fake/metric-b/-95.9910,36.1499/': {
                    u'path': u'/api/citation/fake/metric-b/-95.9910,36.1499/',
                    u'id': u'-95.9910,36.1499',
                    u'year': 2010,
                    u'type': u'fake',
                    u'label': u'Fake Data Citation',
                },
            },
            u'boundaries': {
                u'/api/boundary/fake/metric-a/-95.9910,36.1499/': {
                    u'path': u'/api/boundary/fake/metric-a/-95.9910,36.1499/',
                    u'id': u'-95.9910,36.1499',
                    u'year': 2010,
                    u'type': u'fake',
                    u'label': u'Fake Data Boundary',
                },
                u'/api/boundary/fake/metric-b/-95.9910,36.1499/': {
                    u'path': u'/api/boundary/fake/metric-b/-95.9910,36.1499/',
                    u'id': u'-95.9910,36.1499',
                    u'year': 2010,
                    u'type': u'fake',
                    u'label': u'Fake Data Boundary',
                },
            },
        }
        self.assertResponseDataEqual(expected, response.data)
