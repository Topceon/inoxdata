from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .forms import *


class OrdersHome(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"menu": "trr"}


class VoloknoWork(UpdateView):
    model = Orders
    form_class = UpdateOrderForm
    template_name = 'orders/operator.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'cont'
    # extra_context = {"Machine": "Волокно"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ur'] = f'orders/media/{20}'
        return context

    # def get_material(self):
    #     return Orders.object.get()


class YagWork(DetailView):
    model = Orders
    template_name = 'orders/test.html'
    context_object_name = 'order'

    # def get_queryset(self):
    #     return Orders.objects.filter(machine=2)


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


class DeleteBtn(DeleteView):
    model = Orders
    template_name = 'orders/index.html'
    success_url = reverse_lazy('home')


class UpdateOrderCreator(UpdateView):
    model = Orders
    template_name = 'orders/testord.html'
    form_class = AddOrderForm

class AddTimeReadyForm(CreateView):
    form_class = TimeReadyForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'time_ready'}

