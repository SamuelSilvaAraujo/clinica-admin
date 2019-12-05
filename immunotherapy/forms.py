from django import forms

from .models import Immunotherapy


class ImmunotherapyForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('patient', 'medicine', 'start_date', 'total_applications', )
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'total_applications': forms.NumberInput(attrs={'class': 'form-control'})
        }
