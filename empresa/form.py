from dataclasses import field
from django import forms
from empresa.models import Empresa

class DadosForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        
        widgets = {
            'nome_empresa': forms.TextInput(attrs={ 'class': 'campo', 
                                            'placeholder':'Nome da Empresa'}),
            'tipo': forms.Select(attrs={ 'class': 'campo'}),
            'cidade': forms.Select(attrs={ 'class': 'campo'}),
            'rua': forms.TextInput(attrs={ 'class': 'campo'}),
            'bairro': forms.TextInput(attrs={ 'class': 'campo'}),
            
        }