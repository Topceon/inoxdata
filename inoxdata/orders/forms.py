from django import forms
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
