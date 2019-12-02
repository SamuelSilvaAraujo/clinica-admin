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
