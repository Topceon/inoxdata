from django.http import HttpResponse
from django.shortcuts import render

from .forms import *


def index(request):
    form = AddPart()
    return render(request, 'orders/index.html')


def ready(request):
    return HttpResponse("Готовые детали")
