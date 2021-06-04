from django.urls import path

from .views import *

urlpatterns = [
    path('', OrdersHome.as_view(), name='home'),
    path('ready/', part_form, name='ready'),
    path('forms/', FormCreator.as_view(), name='forms')
]