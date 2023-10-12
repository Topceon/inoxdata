from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, DeleteView, DetailView, UpdateView
from django.db.models import OuterRef, Subquery

from .forms import *


class OrdersHome(ListView):
    paginate_by = 3000
    model = Orders
    template_name = 'orders/index.html'
    extra_context = {"menu": "trr"}

    def get_queryset(self):
        # переменная machine тут захардкожена
        return Orders.objects.filter(priority__gte=1).exclude(machine=2).order_by('id')


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


class ListReadyOrders(ListView):
    paginate_by = 500
    model = Orders
    template_name = 'orders/ready.html'

    def get_queryset(self):
        latest_rdy_parts = ReadyOrders.objects.filter(ready_qty=OuterRef("id")).order_by('-date_time_ready')

        # переменная machine тут захардкожена
        orders_with_latest_ready = Orders.objects.filter(priority=0).exclude(machine=2).annotate(
            latest_ready=Subquery(latest_rdy_parts.values('date_time_ready')[:1])).order_by('-latest_ready')
        return orders_with_latest_ready


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


class AddOtkCheck(View):
    def post(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.otk = False
        order.save()
        return redirect('operator', pk=pk, machinepk=order.machine_id)


class FormMassOrdersCreator(CreateView):
    form_class = AddMassOrdersForm
    template_name = 'orders/forms.html'
    extra_context = {'forms': 'form_mass_orders'}

    def post(self, request):
        form = AddMassOrdersForm(request.POST)
        form = form.save(commit=False)
        machine = Machine.objects.get(name=form.machine)
        name_order_data = form.name_order
        cant_create_orders = []
        with open("create_orders.txt") as my_file:
            file = list(my_file)
        for line in file:
            # print(line)
            need_qty, name_order, part_line = line.strip().split(',')
            print(f'{need_qty},{name_order},{part_line}')
            try:
                part_line = Parts.objects.get(name_part__contains=part_line)
                form.need_qty = 5
                order = Orders(name_order=name_order + " " + name_order_data,
                               part=part_line,
                               need_qty=need_qty,
                               machine=machine,
                               date_for_ready=form.date_for_ready)
                order.save()
            except Exception as e:
                cant_create_orders.append(f'{need_qty},{name_order},{part_line}')
                print(e)
                continue
        if cant_create_orders:
            with open("cant_create_orders.txt", "w") as new_file:
                for item in cant_create_orders:
                    new_file.write(item + "\n")

        return redirect('form_orders')
