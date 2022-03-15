from django.urls import path
from App_Dash import views

app_name = 'App_Dash'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.tva, name='tva'),
    path('health/', views.health, name='health'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('sgbv/', views.sgbv, name='sgbv'),
    path('shelter/', views.shelter, name='shelter'),
    path('site_improvement/', views.site_improvement, name='site_improvement'),
]