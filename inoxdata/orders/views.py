from django.http import HttpResponse
from django.shortcuts import render

from .forms import *


def index(request):
    return HttpResponse("Готовые детали")


def ready(request):
    form = AddPart()
    return render(request, 'orders/ready.html', {'form': form})
