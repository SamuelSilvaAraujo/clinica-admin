from django import forms

from .models import Immunotherapy, Bottle, Application


class ImmunotherapyForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('patient', 'medicine', 'start_date', 'total_bottles', 'illness',)
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'total_bottles': forms.NumberInput(attrs={'class': 'form-control'}),
            'illness': forms.Select(attrs={'class': 'form-control'})
        }


class ImmunotherapyFinisheForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('end_date',)
        widgets = {
            'end_date': forms.DateInput(attrs={'class': 'form-control'})
        }


class StartBottleForm(forms.ModelForm):
    start_date = forms.DateField(label='Data de Inicio', input_formats=['%d/%m/%Y'],
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'}))

    class Meta:
        model = Bottle
        fields = ('number', 'start_date',)
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EndBottleForm(forms.ModelForm):
    end_date = forms.DateField(label='Data de Fim', input_formats=['%d/%m/%Y'],
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'}))

    class Meta:
        model = Bottle
        fields = ('end_date',)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('applicator', 'dosage', 'date',)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'applicator': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
        }
