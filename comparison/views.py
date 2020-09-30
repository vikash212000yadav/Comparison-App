import csv
import pandas as pd
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import *
from .models import *
import json
from . import models
from django.views import generic
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages


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
        if len(form_chipset) >= 2 and form_benchmark is not None:
            chipset = models.Chipset
            benchmark = models.Benchmark
            selected_chipset = []
            for i in form_chipset:
                selected_chipset += chipset.objects.filter(pk=i)

            comparison_values = []
            for test in form_benchmark:
                comparison_values.append(list(benchmark.objects.filter(pk=test)) + list(
                    FilterValue.objects.filter(chipset__id__in=form_chipset, benchmark__id__in=test).values_list(
                        'values', flat=True)))

            return render(request, "comparison/comparison.html",
                          {'form_chipset': form_chipset, 'form_benchmark': form_benchmark, 'values': comparison_values,
                           'chipset_name': selected_chipset})
        else:
            messages.success(request, 'Please select required fields')
            return redirect('comparison:comp')


"""

def convert(request):
    for row in csv.reader(str, delimiter=',', quotechar="|"):
        _, created = Chipset.objects.update_or_create(
            chipset_name=row[1],
        )

        _, created = Benchmark.objects.update_or_create(
            benchmark_name=row[1][1],
        )

        _, created = FilterValue.objects.update_or_create(
            chipset=row[1][2],
        )
"""


def compare(request):
    pass


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been Logged In!')
            return redirect('comparison:comp')
        else:
            messages.success(request, 'Error Logging In - Please Try Again...')
            return redirect('comparison:login')
    else:
        return render(request, 'comparison/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('comparison:comp')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Registered...')
            return redirect('comparison:comp')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'comparison/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Edited Your Profile...')
            return redirect('comparison:comp')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'comparison/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You Have Edited Your Password...')
            return redirect('comparison:comp')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'comparison/change_password.html', context)
