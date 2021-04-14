from django.urls import path

from . import views

app_name = 'sightings-view'

urlpatterns = [
    path('', views.index, name='index'),
    path('sightings/', views.sightings, name='sightings'),

]

