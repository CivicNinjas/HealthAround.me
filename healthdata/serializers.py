from boundaryservice.models import Boundary
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class BoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Boundary
        geo_field = 'shape'
        id_field = 'slug'
        fields = ('slug', 'name', 'display_name', 'external_id', 'kind',
                  'centroid')
