from this import d
from attr import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'age', 'height', 'sex']