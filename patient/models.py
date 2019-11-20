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

    name = models.CharField('Nome', max_length=30)
    birth_date = models.DateField('Data de Nascimento')
    address = models.CharField('Endereço', max_length=100)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=2, choices=STATES_CHOICES)
    phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
    rg = models.CharField('RG', max_length=9, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]
