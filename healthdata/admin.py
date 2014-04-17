from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import ProtoHealth, ScoreMetric, ScoreNode


class ScoreMetricAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'data_source', 'boundary_set', 'data_property', 'algorithm')


class ScoreNodeAdmin(MPTTModelAdmin):
    list_display = ('label', 'slug', 'rel_order', 'weight', 'metric')
    list_editable = ('slug', 'rel_order', 'weight')

admin.site.register(ProtoHealth)
admin.site.register(ScoreMetric, ScoreMetricAdmin)
admin.site.register(ScoreNode, ScoreNodeAdmin)
