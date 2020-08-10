from django import forms
from .models import comententario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = comententario
        fields = '__all__'