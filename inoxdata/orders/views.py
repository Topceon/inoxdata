from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .forms import *


class OrdersHome(ListView):
    model = Parts
    template_name = 'orders/index.html'


class FormCreator(CreateView):
    form_class = AddMaterialForm
    template_name = 'orders/forms.html'


def part_form(request):
    if request.method == 'POST':
        form = AddPartForm(request.POST)
        if form.is_valid():
            try:
                Parts.objects.create(**form.cleaned_data)
                return redirect('ready')
            except:
                form.add_error(None, 'ошибка блин')
    else:
        form = AddPartForm()
    return render(request, 'orders/ready.html', {'Title': 'Создать новую деталь', 'form': form})
