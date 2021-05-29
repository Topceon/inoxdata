from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *


def index(request):
    return HttpResponse("Готовые детали")


def ready(request):
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
    return render(request, 'orders/ready.html', {'form': form})
