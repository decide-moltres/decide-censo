from django.contrib import admin

from .models import Census
from import_export import resources
from import_export.admin import ImportExportModelAdmin

import psycopg2
import xlsxwriter


class CensusResource(resources.ModelResource):
    class Meta:
        model= Census


class CensusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('voting_id', 'voter_id')
    list_filter = ('voting_id', )

    search_fields = ('voter_id', )



admin.site.register(Census, CensusAdmin)
