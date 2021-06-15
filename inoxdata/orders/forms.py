from django import forms
from django.forms import DateInput

from .models import *


class AddPartForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = [
            'name_part',
            'material',
            'thickness',
            'cut_length',
            'cut_input',
            'x_length',
            'y_length',
            'fill_factor',
            'note',
            'otk']


class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = [
            'name_material']


class AddThicknessForm(forms.ModelForm):
    class Meta:
        model = Thickness
        fields = [
            'thickness']


class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'name']


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'name_order',
            'part',
            'need_qty',
            'machine',
            'note',
            'date_for_ready',
            'thickness']
        widgets = {'date_for_ready': DateInput(attrs={'type': 'date'})}  # календарик в форме


class AddCuttingSpeedForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'material',
            'thickness',
            'machine',
            'speed']
