from django import forms
from .models import *


class AddPart(forms.ModelForm):
    class Meta:
        model = Parts
        fields = ['name_part', 'cut_length', 'otk']
