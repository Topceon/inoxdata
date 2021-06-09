from django.urls import path

from .views import *

urlpatterns = [
    path('', OrdersHome.as_view(), name='home'),
    path('ready/', ListReadyOrders.as_view(), name='ready'),
    path('form_materials/', FormCreator.as_view(), name='form_materials'),
    path('form_parts/', FormPartCreator.as_view(), name='form_parts'),
    path('form_orders/', FormOrderCreator.as_view(), name='form_orders'),
    path('form_thickness/', FormThicknessCreator.as_view(), name='form_thickness'),
]
