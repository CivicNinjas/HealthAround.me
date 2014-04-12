from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    list_display = ('boundary', 'state_abbr', 'logical_num')
    raw_id_fields = ('boundary',)


admin.site.register(Census, CensusAdmin)
