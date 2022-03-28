from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# VIEWS:

from django.shortcuts import render


# VIEWS:
def home(request):
    dict = {}
    return render(request, 'home.html', context=dict)

@login_required
def monthlydata(request):
    dict = {}
    return render(request, 'App_Dash/monthlydata.html', context=dict)


@login_required
def servicemapping(request):
    dict = {}
    return render(request, 'App_Dash/servicemapping.html', context=dict)


@login_required
def health(request):
    dict = {}
    return render(request, 'App_Dash/health.html', context=dict)

@login_required
def nutrition(request):
    dict = {}
    return render(request, 'App_Dash/nutrition.html', context=dict)

@login_required
def sgbv(request):
    dict = {}
    return render(request, 'App_Dash/sgbv.html', context=dict)

@login_required
def shelter(request):
    dict = {}
    return render(request, 'App_Dash/shelter.html', context=dict)

@login_required
def site_improvement(request):
    dict = {}
    return render(request, 'App_Dash/site_improvement.html', context=dict)
