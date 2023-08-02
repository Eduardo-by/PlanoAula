# plano_aula/forms.py

from django import forms
from .models import PlanoAula

class PlanoAulaForm(forms.ModelForm):
    class Meta:
        model = PlanoAula
        fields = ['titulo', 'objetivo_geral', 'objetivos_especificos', 'conteudo', 'metodologia','avaliacao','materiais','referencias_basicas','referencias_complementar']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control text-center'}),
            'objetivo_geral': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),
            'objetivos_especificos': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),
            'metodologia': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),     
            'avaliacao': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),     
            'materiais': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),   
            'referencias_basicas': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),   
            'referencias_complementar': forms.Textarea(attrs={'class': 'form-control text-justify', 'rows': 5}),   
        }