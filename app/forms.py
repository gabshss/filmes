from django import forms
from .models import Filme, Serie

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'