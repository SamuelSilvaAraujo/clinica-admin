from django import forms

from .models import *


class MedicineCategoryForm(forms.ModelForm):
    class Meta:
        model = MedicineCategory
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class IllnessForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('name', 'category', 'illness', 'composition', 'volume', 'supplier', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':  'form-control'}),
            'illness': forms.SelectMultiple(attrs={'class': ''}),
            'composition': forms.Textarea(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'})
        }


class LotForm(forms.ModelForm):
    entry_date = forms.DateField(label='Data de Entrada', input_formats=['%d-%m-%Y'],
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'}))

    shelf_life_date = forms.DateField(label='Data de Validade', input_formats=['%d-%m-%Y'],
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'}))

    class Meta:
        model = Lot
        fields = ('medicine', 'amount', 'entry_date', 'shelf_life_date', 'number')
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }


class FreeSampleForm(forms.ModelForm):
    class Meta:
        model = FreeSample
        fields = '__all__'
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'})
        }
