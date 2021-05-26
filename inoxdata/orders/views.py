from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Первая страница")


def ready(request):
    return HttpResponse("Готовые детали")
