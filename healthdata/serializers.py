from boundaryservice.models import Boundary
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import ScoreNode


class BoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Boundary
        geo_field = 'shape'
        id_field = 'slug'
        fields = ('slug', 'name', 'display_name', 'external_id', 'kind',
                  'centroid')


class MetricDetailSerializer(GeoFeatureModelSerializer):
    '''Serialize a boundary's metric to a GeoJSON feature'''

    element = serializers.SerializerMethodField('get_element')

    def get_element(self, obj):
        context = self.context.copy()
        context['boundary'] = obj
        data = ScoreNodeSerializer(context['node'], context=context).data
        return data

    class Meta:
        model = Boundary
        geo_field = 'shape'
        id_field = 'slug'
        fields = ('slug', 'name', 'display_name', 'external_id', 'kind',
                  'centroid', 'element')


class ScoreNodeSerializer(serializers.ModelSerializer):
    '''
    Recursive serializer of ScoreNodes

    This is a 'raw' form of ScoreNode serialization that doesn't calculate
    weighted scores or accumulate boundaries and citations.

    Nodes come in two flavors:

    Branch nodes have children, but no metric.  Their 'children' field
    will be a list of serialized child nodes, and 'metric' will be
    None.

    Leaf nodes have a metric, but no children.  Their 'metric' field will be
    a three-element dictionary of score items, the citation, and the
    boundary, while the 'children' field is an empty list
    '''

    metric = serializers.SerializerMethodField('get_metric')
    children = serializers.SerializerMethodField('get_children')

    class Meta:
        model = ScoreNode
        fields = ('label', 'slug', 'weight', 'metric', 'children')

    def get_children(self, obj):
        '''Return the recursive serialization of child nodes'''
        if obj.is_leaf_node():
            return []
        else:
            return ScoreNodeSerializer(
                obj.children.all().select_related('metric'),
                many=True, context=self.context).data

    def get_metric(self, obj):
        '''Return the metric results of leaf nodes'''
        boundary = self.context.get('boundary')
        location = self.context.get('location')
        cache = self.context.get('cache')
        if boundary:
            metric = obj.score_by_boundary(boundary, cache)
        elif location:
            metric = obj.score_by_location(location, cache)
        else:
            return None
        assert metric or not obj.is_leaf_node()
        return metric
