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


class ApplicationUpdateForm(forms.ModelForm):
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


class ApplicationCreateForm(forms.Form):
    application_date = forms.DateField(label="Data da Aplicação", input_formats=['%d-%m-%Y'],
                                       widget=forms.DateInput(attrs={'class': 'form-control',
                                                                     'placeholder': '__/__/____'})
                                       )
    applicator = forms.CharField(label="Aplicador",
                                 widget=forms.TextInput(attrs={'class': 'form-control'})
                                 )
    dosage = forms.CharField(label="Dosagem",
                             widget=forms.TextInput(attrs={'class': 'form-control'})
                             )
    bottle_number = forms.IntegerField(label="Frasco",
                                       widget=forms.NumberInput(attrs={'class': 'form-control'})
                                       )
    application_number = forms.IntegerField(label="Dose",
                                            widget=forms.NumberInput(attrs={'class': 'form-control'})
                                            )
    appointment_date = forms.DateField(label='Data', input_formats=['%d-%m-%Y'],
                                       widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': '__/__/____'})
                                       )
    appointment_start_hour = forms.TimeField(label='Hora de Inicio', input_formats=['%H:%M'],
                                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': '__:__'})
                                             )
    appointment_end_hour = forms.TimeField(label='Hora de Fim', input_formats=['%H:%M'],
                                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': '__:__'})
                                           )
    appointment_notes = forms.CharField(label="Descrição",
                                        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))


class TagPdfForm(forms.Form):
    patient = forms.CharField(label="Paciente", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bottle_number = forms.IntegerField(label="Frasco", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    concentration = forms.CharField(label="Concentração", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    period = forms.CharField(label="Periodo", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dimensions = forms.CharField(max_length=10, widget=forms.HiddenInput())
