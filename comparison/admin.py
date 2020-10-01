from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(Benchmark)
@admin.register(Chipset)
@admin.register(FilterValue)
class AdminView(ImportExportModelAdmin):
    pass
