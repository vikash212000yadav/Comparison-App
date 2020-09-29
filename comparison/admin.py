from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(Benchmark)
@admin.register(Chipset)
@admin.register(FilterValue)
class AdminView(ImportExportModelAdmin):
    exclude = ["id"]
