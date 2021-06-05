from django.urls import path

from .views import *

urlpatterns = [
    path('', OrdersHome.as_view(), name='home'),
    path('ready/', ListReadyOrders.as_view(), name='ready'),
    path('forms/', FormCreator.as_view(), name='forms'),
    path('form_parts/', FormPartCreator.as_view(), name='form_parts'),
    path('form_orders/', FormOrderCreator.as_view(), name='form_orders')
]
