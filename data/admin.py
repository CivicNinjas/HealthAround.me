from django.contrib import admin

from .models import Census, Dartmouth


class CensusAdmin(admin.ModelAdmin):
    list_display = ('boundary', 'state_abbr', 'logical_num')
    raw_id_fields = ('boundary',)


class DartmouthAdmin(admin.ModelAdmin):
    list_display = ('boundary', )
    raw_id_fields = ('boundary', )

admin.site.register(Census, CensusAdmin)
admin.site.register(Dartmouth, DartmouthAdmin)
