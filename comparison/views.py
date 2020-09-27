from django.shortcuts import render
from django.views.generic import ListView

from .forms import FilterForm

from .models import *
import json
from . import models
from django.views import generic


# Create your views here.

def home(request):
    if request.method == "GET":
        choices_chipset = list(Chipset.objects.values_list('id', 'chipset_name'))
        choices_benchmark = list(Benchmark.objects.values_list('id', 'benchmark_name'))

        form = FilterForm(choices_chipset=choices_chipset,
                          choices_benchmark=choices_benchmark)

        return render(request, "comparison/home.html", {'form': form})

    if request.method == "POST" and 'submit' in request.POST:
        form_chipset = request.POST.getlist("Chipset") or None
        form_benchmark = request.POST.getlist("Benchmark") or None
        comparison_values = list(
            FilterValue.objects.filter(chipset__id__in=form_chipset, benchmark__id__in=form_benchmark).values_list(
                'values', flat=True))
        return render(request, "comparison/comparison.html",
                      {'form_chipset': form_chipset, 'form_benchmark': form_benchmark, 'values': comparison_values})


def compare(request):
    pass
