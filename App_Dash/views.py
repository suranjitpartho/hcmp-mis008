from django.shortcuts import render

# VIEWS:

from django.shortcuts import render


# VIEWS:
def home(request):
    dict = {}
    return render(request, 'home.html', context=dict)

def tva(request):
    dict = {}
    return render(request, 'App_Dash/tva.html', context=dict)

def health(request):
    dict = {}
    return render(request, 'App_Dash/health.html', context=dict)

def nutrition(request):
    dict = {}
    return render(request, 'App_Dash/nutrition.html', context=dict)

def sgbv(request):
    dict = {}
    return render(request, 'App_Dash/sgbv.html', context=dict)

def shelter(request):
    dict = {}
    return render(request, 'App_Dash/shelter.html', context=dict)

def site_improvement(request):
    dict = {}
    return render(request, 'App_Dash/site_improvement.html', context=dict)
