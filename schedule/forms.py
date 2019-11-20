from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField()

    class Meta:
        model = Appointment
        fields = ('patient', 'start', 'end', 'date', )
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'start': forms.TimeInput(attrs={'class': 'form-control'}),
            'end': forms.TimeInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'})
        }
