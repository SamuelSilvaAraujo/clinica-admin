from django.db import models


class Patient(models.Model):
    STATES_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

    name = models.CharField('Nome', max_length=150)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)
    address = models.CharField('Endereço', max_length=100, null=True, blank=True)
    city = models.CharField('Cidade', max_length=50, null=True, blank=True)
    state = models.CharField('Estado', max_length=2, choices=STATES_CHOICES, null=True, blank=True)
    phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
    rg = models.CharField('RG', max_length=9, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    convenio = models.CharField('Convênio', max_length=50)
    photo = models.ImageField('foto', blank=True, null=True, upload_to="patient_photo")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
