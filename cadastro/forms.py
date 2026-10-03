from django import forms

from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'idade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'campo', 'placeholder': 'voce@exemplo.com'}),
            'idade': forms.NumberInput(attrs={'class': 'campo', 'min': 0}),
        }
