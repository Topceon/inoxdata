from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .forms import *


class OrdersHome(ListView):
    model = Parts
    template_name = 'orders/index.html'


class ListReadyOrders(ListView):
    model = ReadyOrders
    template_name = 'orders/ready.html'


class FormCreator(CreateView):
    form_class = AddMaterialForm
    template_name = 'orders/forms.html'


class FormPartCreator(CreateView):
    form_class = AddPartForm
    template_name = 'orders/form_parts.html'


class FormOrderCreator(CreateView):
    form_class = AddOrderForm
    template_name = 'orders/form_orders.html'
