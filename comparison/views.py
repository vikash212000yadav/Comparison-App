import form as form
from django.shortcuts import render
from django.views.generic import ListView

from .forms import FilterForm

from .models import FilterChoices
import json
from . import models
from django.views import generic


# Create your views here.


def home(request):
    db_choices = FilterChoices.objects.all()[0]
    if request.method == "GET":
        jsonDec = json.decoder.JSONDecoder()
        # choices_company = [(i, i) for i in jsonDec.decode(db_choices.company)]
        choices_chipset = [(i, i) for i in jsonDec.decode(db_choices.chipset)]
        choices_benchmark = [(i, i) for i in jsonDec.decode(db_choices.benchmark)]

        form = FilterForm(choices_chipset=choices_chipset,
                          choices_benchmark=choices_benchmark)

        return render(request, "comparison/home.html", {'form': form})

    if request.method == "POST" and 'submit' in request.POST:
        # form_company = request.POST["Company"] or None
        form_chipset = request.POST["Chipset"] or None
        form_benchmark = request.POST["Benchmark"] or None
        return render(request, "comparison/comparison.html",
                      {'form_chipset': form_chipset, 'form_benchmark': form_benchmark})


def compare(request):
    pass
