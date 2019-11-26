from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(label='Data', input_formats=['%d-%m-%Y'],
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__/__/____'}))
    start_hour = forms.TimeField(label='Hora de Inicio', input_formats=['%H:%M'],
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__:__'}))
    end_hour = forms.TimeField(label='Hora de Fim', input_formats=['%H:%M'],
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '__:__'}))

    class Meta:
        model = Appointment
        fields = ('patient', 'start_hour', 'end_hour', 'date', 'notes', )
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
