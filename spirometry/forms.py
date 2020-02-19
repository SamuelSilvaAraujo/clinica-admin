from django import forms

from .models import Material, Stock, Spirometry


class SpirometryForm(forms.ModelForm):
    class Meta:
        model = Spirometry
        fields = ['patient', 'date', ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class MaterialStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['material', 'date', 'amount', ]
        widgets = {
            'material': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
