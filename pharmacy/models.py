from django.db import models

from patient.models import Patient


class Illness(models.Model):
    name = models.CharField('Doença', max_length=100)

    def __str__(self):
        return self.name


class MedicineCategory(models.Model):
    name = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField('Remédio', max_length=100)
    category = models.ForeignKey(MedicineCategory, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    illness = models.ManyToManyField(Illness, verbose_name='Doenças', blank=True)
    composition = models.TextField('Composição')
    volume = models.CharField('Volume', max_length=10)
    supplier = models.CharField('Fornecedor', max_length=200)

    def __str__(self):
        return self.name

    def total_in_stock(self):
        total = 0
        for lot in self.lot_set.all():
            total += lot.amount
        for immunotherapy in self.immunotherapy_set.all():
            total -= immunotherapy.bottle_set.count()
        total -= self.freesample_set.count()
        return total


class Lot(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Remédio')
    amount = models.IntegerField('Quantidade')
    entry_date = models.DateField('Data de Entrada')
    shelf_life_date = models.DateField('Data de Validade')

    class Meta:
        ordering = ['entry_date', 'shelf_life_date']

    def __str__(self):
        return "{} ({})".format(self.medicine.name, self.amount)


class FreeSample(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Medicamento')
    date = models.DateField('Data')

    def __str__(self):
        return "{} - {}".format(self.medicine.name, self.patient.name)
