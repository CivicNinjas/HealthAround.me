import json

from .base import APITestCase
from healthdata.algorithms import AlgorithmCache
from healthdata.models import Boundary, ScoreNode, ScoreMetric
from healthdata.serializers import (
    MetricDetailSerializer, ScoreNodeSerializer)


class MetricDetailSerializerTest(APITestCase):
    def setUp(self):
        self.parent_node = ScoreNode.objects.create(
            slug='parent', label='Parent', weight=1, parent=None)
        self.metric_a = ScoreMetric.objects.create(
            name=u'Metric A', description=u'The first metric',
            algorithm=ScoreMetric.PLACEHOLDER_ALGORITHM, params={})
        self.node_a = ScoreNode.objects.create(
            slug='metric-a', label='Metric A', metric=self.metric_a, weight=2,
            parent=self.parent_node)

    def test_detail_fake_boundary(self):
        shape = (
            "MULTIPOLYGON(((-95.99 36.15, -95.99 36.16, -95.98 36.16,"
            " -95.98 36.15, -95.99 36.15)))")
        centroid = "POINT(-95.985 36.155)"
        fake_boundary = Boundary(
            shape=shape, centroid=centroid, name='fake',
            display_name='Pending Data', kind='Pending Data',
            slug='fake_2_-95.99_36.15')
        serializer = MetricDetailSerializer(
            fake_boundary, context={'node': self.node_a})
        expected = {
            u'id': u'fake_2_-95.99_36.15',
            u'type': u'Feature',
            u'geometry': {
                u'type': u'MultiPolygon',
                u'coordinates': [[[
                    [-95.99, 36.15],
                    [-95.99, 36.16],
                    [-95.98, 36.16],
                    [-95.98, 36.15],
                    [-95.99, 36.15],
                ]]]},
            u'properties': {
                u'name': u'fake',
                u'display_name': u'Pending Data',
                u'external_id': u'',
                u'kind': u'Pending Data',
                u'centroid': {
                    u'type': u'Point',
                    u'coordinates': [-95.985, 36.155],
                },
                u'element': {
                    u'label': u'Metric A',
                    u'slug': u'metric-a',
                    u'weight': 2,
                    u'metric': {
                        u'summary': {
                            u'score': 0.46,
                            u'value': 0.36,
                            u'value_type': u'percent',
                            u'description': u'The first metric',
                        },
                        u'detail': {
                            u'path': (
                                u'/api/detail/fake_2_-95.99_36.15/metric-a/'),
                            u'score_text': self.score_text_no_data('Metric A'),
                        },
                        u'boundary': {
                            u'path': u'/api/boundary/fake_2_-95.99_36.15/',
                            u'label': u'Future Data Placeholder',
                            u'type': u'Placeholder',
                        },
                    },
                    u'children': [],
                },
            }
        }
        self.assertSerializerDataEqual(expected, serializer.data)


class ScoreSerializerTest(APITestCase):
    def setUp(self):
        self.grandma_node = ScoreNode.objects.create(
            slug='grandma', label='Grandma', weight=1)
        self.parent_node = ScoreNode.objects.create(
            slug='parent', label='Parent', weight=1, parent=self.grandma_node)
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
        self.context = {
            'location': (-95.991, 36.1499),
            'cache': AlgorithmCache(),
        }

    def assertSerializerDataEqual(self, expected, actual):
        '''
        assert serializer.data is equal to a dictionary

        Because serializer.data includes dict-like objects that aren't quite
        dicts, it passed through json encoding/decoding first, to get a
        plain old dict (with unicode strings)
        '''
        data = json.loads(json.dumps(actual))
        self.assertEqual(expected, data)

    def boundary_rep(self):
        '''Boundary for first metric'''
        return {
            u'path': u'/api/boundary/fake_2_-96.00_36.14/',
            u'label': u'Future Data Placeholder',
            u'type': u'Placeholder',
        }

    def metric_a_rep(self):
        '''Raw representation of first metric'''
        return {
            u"label": u"Metric A",
            u"slug": u"metric-a",
            u"weight": 2,
            u"metric": {
                u'summary': {
                    u"score": 0.35,
                    u"value": 0.2,
                    u"value_type": u"percent",
                    u"description": u"The first metric",
                },
                u'detail': {
                    u"path": u"/api/detail/fake_2_-96.00_36.14/metric-a/",
                    u'score_text': self.score_text_no_data('Metric A'),
                },
                u'boundary': self.boundary_rep(),
            },
            u"children": [],
        }

    def metric_b_rep(self):
        return {
            u"label": u"Metric B",
            u"slug": u"metric-b",
            u"weight": 1,
            u"metric": {
                u'summary': {
                    u"score": 0.8,
                    u"value": 0.87,
                    u"value_type": u"percent",
                    u"description": u"The second metric",
                },
                u'detail': {
                    u"path": u"/api/detail/fake_2_-96.00_36.14/metric-b/",
                    u'score_text': self.score_text_no_data('Metric B'),
                },
                u'boundary': self.boundary_rep(),
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
