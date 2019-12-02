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
