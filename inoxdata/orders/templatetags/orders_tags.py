from django import template
from orders.models import *

register = template.Library()


# ======= формирование списка для оператора ===========
@register.inclusion_tag('orders/list_orders.html')
def get_orders(machine=1, sel=0):
    ords = Orders.objects.filter(priority__gte=1, machine=machine).order_by('priority')
    if sel == 1:
        ords = None
    return {"ords": ords, 'sel': sel}


# ======= формирование списка станков с первой  ===========
@register.inclusion_tag('orders/list_machine.html')
def change_machine(sel=0):
    mach = Machine.objects.all()
    return {'mach': mach, 'sel': sel}


@register.inclusion_tag('orders/header.html')
def show_header():
    pass

@register.inclusion_tag('orders/header2.html')
def show_header2():
    pass
