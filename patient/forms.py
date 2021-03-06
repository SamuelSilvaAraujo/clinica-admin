from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        CONVENIO_CHOICES = [
            ('UNIMED', 'UNIMED'),
            ('SUS', 'SUS'),
            ('PARTICULAR', 'PARTICULAR'),
            ('CRIA', 'CRIA'),
            ('OUTROS', 'OUTROS'),
        ]

        model = Patient
        fields = ('name', 'birth_date', 'phone', 'rg', 'cpf', 'address', 'state', 'city', 'convenio', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'convenio': forms.Select(attrs={'class': 'form-control'}, choices=CONVENIO_CHOICES)
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('photo', )
        widgets = {
            'photo': forms.FileInput()
        }
