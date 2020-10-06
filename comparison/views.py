from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *
import json
from . import models
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.
def all_users(request):
    users = User.objects.values_list('first_name', 'email', flat=False)
    superuser = User.objects.filter(is_superuser=True).values_list('first_name', 'email')
    staff = User.objects.filter(is_staff=True, is_superuser=False).values_list('first_name', 'email')
    normal_user = User.objects.filter(is_active=True, is_staff=False).values_list('first_name', 'email')
    return render(request, 'comparison/user_list.html',
                  {'users': users, 'superusers': superuser, 'staff': staff, 'normal_user': normal_user})


def home(request):
    if request.method == "GET":
        choices_chipset = list(Chipset.objects.values_list('id', 'chipset_name'))
        choices_benchmark = list(Benchmark.objects.values_list('id', 'benchmark_name'))

        form = FilterForm(choices_chipset=choices_chipset,
                          choices_benchmark=choices_benchmark)

        return render(request, "comparison/home.html", {'form': form})

    if request.method == "POST" and 'submit' in request.POST:
        form_chipset = request.POST.getlist("Chipset") or None  # selected chipset id's in a list
        form_benchmark = request.POST.getlist("Benchmark") or None  # selected benchmark id's in a list
        if len(form_chipset) >= 2 and form_benchmark is not None:
            # validations to select minimum 2 chipsets and minimum one benchmark
            chipset = models.Chipset  # fetching full Chipset table from models.py
            benchmark = models.Benchmark  # fetching full benchmark table from models.py
            selected_chipset = []  # blank list to store selected chipsets name
            for i in form_chipset:
                selected_chipset += chipset.objects.filter(pk=i)
                # selected chipset's name list fetched from chipset table as per the selected ids
                # selected_chipset = ['<Chipset: SA6155>', '<Chipset: SA6155A>']

            comparison_values = []  # selected benchmarks name + values
            for test in form_benchmark:
                comparison_values.append(list(benchmark.objects.filter(pk=test)) + list(
                    FilterValue.objects.filter(chipset__id__in=form_chipset, benchmark__id__in=test).values_list(
                        'final_values', flat=True)))
            # comparison_values=['<Benchmark: Antutu 7>', 100, 130], ['<Benchmark: Antutu 6>', 102, 132]]

            selected_chipset1 = ['Chipsets']
            for i in form_chipset:
                selected_chipset1 += chipset.objects.filter(pk=i).values_list('chipset_name', flat=True)

            comparison_values1 = [selected_chipset1]
            for test in form_benchmark:
                comparison_values1.append(
                    list(benchmark.objects.filter(pk=test).values_list('benchmark_name', flat=True)) + list(
                        FilterValue.objects.filter(chipset__id__in=form_chipset, benchmark__id__in=test).values_list(
                            'final_values', flat=True)))

            test1 = json.dumps(transpose(comparison_values1, []))

            return render(request, "comparison/comparison.html",
                          {'form_chipset': form_chipset, 'form_benchmark': form_benchmark,
                           'final_values': comparison_values,
                           'chipset_name': selected_chipset, 'test1': test1})
        else:
            messages.success(request, 'Please select required fields')
            return redirect('comparison:comp')


def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


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
