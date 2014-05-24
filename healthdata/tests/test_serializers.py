import json

from rest_framework.test import APITestCase

from healthdata.models import ScoreNode, ScoreMetric
from healthdata.serializers import ScoreNodeSerializer


class ScoreSerializerTest(APITestCase):
    maxDiff = None

    def setUp(self):
        self.grandma_node = ScoreNode.objects.create(
            slug='grandma', label='Grandma', weight=1)
        self.parent_node = ScoreNode.objects.create(
            slug='parent', label='Parent', weight=1, parent=self.grandma_node)
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
        self.context = {'location': (-95.991, 36.1499)}

    def assertSerializerDataEqual(self, expected, actual):
        '''
        assert serializer.data is equal to a dictionary

        Because serializer.data includes dict-like objects that aren't quite
        dicts, it passed through json encoding/decoding first, to get a
        plain old dict (with unicode strings)
        '''
        data = json.loads(json.dumps(actual))
        self.assertEqual(expected, data)

    def boundary_a_rep(self):
        '''Boundary for first metric'''
        return {
            u'path': u'/api/boundary/fake/metric-a/-95.9910,36.1499/',
            u'id': u'-95.9910,36.1499',
            u'label': u'Fake Data Boundary',
            u'type': u'fake',
            u'year': 2010,
        }

    def boundary_b_rep(self):
        '''Boundary for second metric'''
        return {
            u'path': u'/api/boundary/fake/metric-b/-95.9910,36.1499/',
            u'id': u'-95.9910,36.1499',
            u'label': u'Fake Data Boundary',
            u'type': u'fake',
            u'year': 2010,
        }

    def citation_a_rep(self):
        '''Citation for first metric'''
        return {
            u'path': u'/api/citation/fake/metric-a/-95.9910,36.1499/',
            u'id': u'-95.9910,36.1499',
            u'label': u'Fake Data Citation',
            u'type': u'fake',
            u'year': 2010,
        }

    def citation_b_rep(self):
        '''Citation for second metric'''
        return {
            u'path': u'/api/citation/fake/metric-b/-95.9910,36.1499/',
            u'id': u'-95.9910,36.1499',
            u'label': u'Fake Data Citation',
            u'type': u'fake',
            u'year': 2010,
        }

    def metric_a_rep(self):
        '''Raw representation of first metric'''
        return {
            u"label": u"Metric A",
            u"slug": u"metric-a",
            u"weight": 2,
            u"metric": {
                u'score': {
                    u"score": 0.73,
                    u"value": 0.61,
                    u"value_type": u"percent",
                    u"description": u"The first metric",
                    u"citation_path": (
                        u"/api/citation/fake/metric-a/-95.9910,36.1499/"),
                    u"boundary_path": (
                        u"/api/boundary/fake/metric-a/-95.9910,36.1499/"),
                },
                u'citation': self.citation_a_rep(),
                u'boundary': self.boundary_a_rep(),
            },
            u"children": [],
        }

    def metric_b_rep(self):
        return {
            u"label": u"Metric B",
            u"slug": u"metric-b",
            u"weight": 1,
            u"metric": {
                u'score': {
                    u"score": 0.78,
                    u"value": 0.2,
                    u"value_type": u"percent",
                    u"description": u"The second metric",
                    u"citation_path": (
                        u"/api/citation/fake/metric-b/-95.9910,36.1499/"),
                    u"boundary_path": (
                        u"/api/boundary/fake/metric-b/-95.9910,36.1499/"),
                },
                u'citation': self.citation_b_rep(),
                u'boundary': self.boundary_b_rep(),
            },
            u"children": [],
        }

    def parent_node_rep(self):
        '''Raw representation of parent branch node'''
        return {
            u"label": u"Parent",
            u"slug": u"parent",
            u"weight": 1,
            u"metric": None,
            u"children": [
                self.metric_a_rep(),
                self.metric_b_rep(),
            ],
        }

    def test_first_metric_node(self):
        serializer = ScoreNodeSerializer(self.node_a, context=self.context)
        expected = self.metric_a_rep()
        self.assertSerializerDataEqual(expected, serializer.data)

    def test_second_metric_node(self):
        serializer = ScoreNodeSerializer(self.node_b, context=self.context)
        expected = self.metric_b_rep()
        self.assertSerializerDataEqual(expected, serializer.data)

    def test_sibling_nodes(self):
        serializer = ScoreNodeSerializer(
            [self.node_a, self.node_b], many=True, context=self.context)
        expected = [self.metric_a_rep(), self.metric_b_rep()]
        self.assertSerializerDataEqual(expected, serializer.data)

    def test_parent_node(self):
        serializer = ScoreNodeSerializer(
            self.parent_node, context=self.context)
        expected = self.parent_node_rep()
        self.assertSerializerDataEqual(expected, serializer.data)

    def test_grandma_node(self):
        serializer = ScoreNodeSerializer(
            self.grandma_node, context=self.context)
        expected = {
            u"label": u"Grandma",
            u"slug": u"grandma",
            u"weight": 1,
            u"metric": None,
            u"children": [self.parent_node_rep()],
        }
        self.assertSerializerDataEqual(expected, serializer.data)
