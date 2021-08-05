from django.urls import path

from .views import *

urlpatterns = [
    path('', OrdersHome.as_view(), name='work'),
    path('operator/<int:machinepk>/<int:pk>/', OperatorWork.as_view(), name='operator'),
    path('ready/', ListReadyOrders.as_view(), name='ready'),
    path('form-materials/', FormCreator.as_view(), name='form_materials'),
    path('form-parts/', FormPartCreator.as_view(), name='form_parts'),
    path('form-orders/', FormOrderCreator.as_view(), name='form_orders'),
    path('form-thickness/', FormThicknessCreator.as_view(), name='form_thickness'),
    path('form-machine/', FormMachineCreator.as_view(), name='form_machine'),
    path('form-cutting_speed/', FormCuttingSpeedCreator.as_view(), name='form_cutting_speed'),
    path('delete/<int:pk>/', DeleteBtn.as_view(), name='delete'),
    path('test-order/<int:pk>/', UpdateOrderCreator.as_view(), name='test_order'),
    path('form-time_ready/', AddTimeReadyForm.as_view(), name='time_ready'),
    path('date-ready/<int:pk>/', AddDateReady.as_view(), name='date_ready'),

]
