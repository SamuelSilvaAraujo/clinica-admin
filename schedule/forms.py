from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Appointment
        fields = ('patient', 'start', 'end', 'date', 'notes', )
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'start': forms.TimeInput(attrs={'class': 'form-control'}),
            'end': forms.TimeInput(attrs={'class': 'form-control'}),
            # 'date': forms.DateInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
