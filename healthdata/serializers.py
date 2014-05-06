import random

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


class ScoreSerializer(serializers.ModelSerializer):
    elements = serializers.RelatedField(source='children')
    score = serializers.SerializerMethodField('get_score')

    class Meta:
        model = ScoreNode
        fields = ('label', 'slug', 'weight', 'score', 'elements')

    def get_score(self, obj):
        return random.random()


class TertiaryScoreSerializer(serializers.ModelSerializer):
    description = serializers.Field(source='metric.description')
    score = serializers.SerializerMethodField('get_score')
    value = serializers.SerializerMethodField('get_value')
    value_type = serializers.SerializerMethodField('get_value_type')
    citation_path = serializers.SerializerMethodField('get_citation_path')
    boundary_path = serializers.SerializerMethodField('get_boundary_path')

    class Meta:
        model = ScoreNode
        fields = ('label', 'slug',  'weight', 'score', 'value', 'value_type',
                  'description', 'citation_path', 'boundary_path')

    def get_score(self, obj):
        return random.random()

    def get_value(self, obj):
        return random.random() * 100

    def get_value_type(self, obj):
        return 'percent'

    def get_citation_path(self, obj):
        return '/api/citation/fake/access-to-jobs/'

    def get_boundary_path(self, obj):
        return '/api/boundary/fake/access-to-jobs/'


class SecondaryScoreSerializer(ScoreSerializer):
    elements = TertiaryScoreSerializer(source='children')


class PrimaryScoreSerializer(ScoreSerializer):
    elements = SecondaryScoreSerializer(source='children')

    def __init__(self, *args, **kwargs):
        self.location = kwargs.pop('location', (None, None))
        super(PrimaryScoreSerializer, self).__init__(*args, **kwargs)
