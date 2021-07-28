from django import template
from orders.models import *

register = template.Library()


# ======= формирование списка для оператора ===========
@register.inclusion_tag('orders/list_orders.html')
def get_orders(machine=1, sel=0):
        ords = Orders.objects.filter(priority=100, machine=machine)
        if sel == 0:
            sel = ords[0].id
        return {"ords": ords, 'sel': sel}


# ======= формирование списка станков с первой  ===========
@register.inclusion_tag('orders/list_machine.html')
def change_machine():
    mach = Machine.objects.all()
    return {'mach': mach}


@register.inclusion_tag('orders/header.html')
def show_header():
    pass
