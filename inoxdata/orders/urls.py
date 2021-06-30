from django.urls import path

from .views import *

urlpatterns = [
    path('', OrdersHome.as_view(), name='home'),
    path('volokno/', VoloknoWork.as_view(), name='volokno'),
    path('yag/', YagWork.as_view(), name='yag'),
    path('gidro/', GidroWork.as_view(), name='gidro'),
    path('ready/', ListReadyOrders.as_view(), name='ready'),
    path('form_materials/', FormCreator.as_view(), name='form_materials'),
    path('form_parts/', FormPartCreator.as_view(), name='form_parts'),
    path('form_orders/', FormOrderCreator.as_view(), name='form_orders'),
    path('form_thickness/', FormThicknessCreator.as_view(), name='form_thickness'),
    path('form_machine/', FormMachineCreator.as_view(), name='form_machine'),
    path('form_cutting_speed/', FormCuttingSpeedCreator.as_view(), name='form_cutting_speed'),
    path('delete/<int:pk>', DeleteBtn.as_view(), name='delete'),
    path('test-order/<int:pk>', UpdateOrderCreator.as_view(), name='test_order')
]
