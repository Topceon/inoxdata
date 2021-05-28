from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('ready/', ready, name='ready')
]