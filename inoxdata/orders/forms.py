from django import forms
from django.forms import DateInput

from .models import *


class AddPartForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = [
            'name_part',
            'material',
            'x_length',
            'y_length',
            'fill_factor',
            'cut_length',
            'cut_input',
            'otk']


class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = [
            'name_material',
            'thickness_material',
            'fiber_speed',
            'yag_speed',
            'gidro_speed']


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'nameOrder',
            'part',
            'need_qty',
            'note',
            'date_for_ready']
        widgets = {
            'date_for_ready': DateInput(attrs={'type': 'date'}) # календарик в форме
        }

