from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources


@admin.register(Benchmark)
@admin.register(Chipset)
@admin.register(FilterValue)
class AdminView(ImportExportModelAdmin):
    pass
    #exclude = ('id',)


"""
class ChipsetResource(resources.ModelResource):
    class Meta:
        model = Chipset
        # fields = ('chipset_name',)


class BenchmarkResource(resources.ModelResource):
    class Meta:
        model = Benchmark
        fields = 'Unnamed: 0'


class ValueResource(resources.ModelResource):
    class Meta:
        model = FilterValue
        fields = ('value', 'benchmark_id', 'chipset_id')


class ChipsetAdmin(ImportExportModelAdmin):
    resource_class = ChipsetResource


class BenchmarkAdmin(ImportExportModelAdmin):
    resource_class = BenchmarkResource
    exclude = ('id', )


class ValueAdmin(ImportExportModelAdmin):
    resource_class = ValueResource


admin.site.register(Chipset, ChipsetAdmin)
admin.site.register(Benchmark, BenchmarkAdmin)
admin.site.register(FilterValue, ValueAdmin)
"""