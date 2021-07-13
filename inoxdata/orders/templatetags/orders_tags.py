from django import template
from orders.models import *

register = template.Library()


# ======= формирование списка для оператора ===========
@register.inclusion_tag('orders/list_orders.html')
def get_orders(sel=24):
        ords = Orders.objects.all()
        return {"ords": ords, 'sel': sel}


# ======= формирование детали для оператора ===========
@register.inclusion_tag('orders/detail_order.html')
def show_order(pk=23):
    if pk == 23:
        ords = Orders.objects.get(pk=23)
    else:
        ords = Orders.objects.get(pk=pk)
        return {"ords": ords}


@register.inclusion_tag('orders/header.html')
def show_header():
    pass
