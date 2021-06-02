from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('ready/', part_form, name='ready'),
    path('forms/', material_form, name='forms')
]