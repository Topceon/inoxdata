from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .forms import *


class OrdersHome(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"menu": "trr"}


class VoloknoWork(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"Machine": "Волокно"}

    def get_queryset(self):
        return Orders.objects.filter(machine=1)


class YagWork(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"Machine": "YAG"}

    def get_queryset(self):
        return Orders.objects.filter(machine=2)


class GidroWork(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"Machine": "Гидра"}

    def get_queryset(self):
        return Orders.objects.filter(machine=3)


class ListReadyOrders(ListView):
    model = ReadyOrders
    template_name = 'orders/ready.html'


class FormCreator(CreateView):
    form_class = AddMaterialForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_materials'}


class FormThicknessCreator(CreateView):
    form_class = AddThicknessForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_thickness'}


class FormPartCreator(CreateView):
    form_class = AddPartForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_parts'}


class FormOrderCreator(CreateView):
    form_class = AddOrderForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_orders'}


class FormMachineCreator(CreateView):
    form_class = AddMachineForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_machine'}


class FormCuttingSpeedCreator(CreateView):
    form_class = AddCuttingSpeedForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_cutting_speed'}
