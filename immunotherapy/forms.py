from django import forms

from .models import Immunotherapy, Application


class ImmunotherapyForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('patient', 'medicine', 'start_date', 'total_applications', 'total_bottles', 'illness',)
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'total_bottles': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_applications': forms.NumberInput(attrs={'class': 'form-control'}),
            'illness': forms.Select(attrs={'class': 'form-control'})
        }


class ImmunotherapyFinisheForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('end_date',)
        widgets = {
            'end_date': forms.DateInput(attrs={'class': 'form-control'})
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('applicator', 'dosage', 'date', 'bottle_number', 'application_number', )
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'applicator': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'bottle_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'application_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
