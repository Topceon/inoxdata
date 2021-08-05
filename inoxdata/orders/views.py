from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, DeleteView, DetailView, UpdateView

from .forms import *


class OrdersHome(ListView):
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"menu": "trr"}


class OperatorWork(DetailView):
    model = Orders
    form_class = DateReadyForm
    template_name = 'orders/operator.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'cont'

    def get_context_data(self, *, object=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machinepk'] = self.kwargs['machinepk']
        return context




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
    model = Orders
    template_name = 'orders/ready.html'

    def get_queryset(self):
        return Orders.objects.filter(priority=0)


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
    success_url = reverse_lazy('work')


class UpdateOrderCreator(UpdateView):
    model = Orders
    template_name = 'orders/testord.html'
    form_class = AddOrderForm

class AddTimeReadyForm(CreateView):
    form_class = TimeReadyForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'time_ready'}


class AddDateReady(View):
    def post(self, request, pk):
        form = AddReadyForm(request.POST)
        order = Orders.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.machine = order.machine
            if not form.qty:
                form.qty = order.need_qty - int(order.get_ready_qty())
            form.ready_qty = order
            form.save()
        return redirect('operator', pk=pk, machinepk=order.machine_id)
