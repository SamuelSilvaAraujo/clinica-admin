from django import forms

from .models import Immunotherapy, Bottle, Application


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


class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ('bottle_number', 'lot', )
        widgets = {
            'bottle_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'lot': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        immunotherapy = kwargs.pop('immunotherapy')
        super(BottleForm, self).__init__(*args, **kwargs)
        self.fields['lot'].queryset = immunotherapy.medicine.lot_set.all_in_stock()


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('bottle',  'applicator', 'dosage', 'date', )
        widgets = {
            'bottle': forms.Select(attrs={'class': 'form-control'}),
            'applicator': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }
