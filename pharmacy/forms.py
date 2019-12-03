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
        fields = ('name', 'category', 'illness', 'composition', 'volume', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':  'form-control'}),
            'illness': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'composition': forms.Textarea(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'})
        }


class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ('medicine', 'amount', 'entry_date', 'shelf_life_date', 'number')
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control'}),
            'shelf_life_date': forms.DateInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
