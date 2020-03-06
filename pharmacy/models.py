from django.utils import timezone

from django.db import models
from django.db.models import Count, F

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
    volume = models.FloatField('Volume')
    supplier = models.CharField('Fornecedor', max_length=200)

    def __str__(self):
        return self.name


class LotQuerySet(models.QuerySet):
    def all_in_stock_queryset(self):
        return self.annotate(current_amount=F('amount') - (Count('bottle') + Count('medicine__freesample'))).filter(current_amount__gt=0)


class LotManager(models.Manager):
    def get_queryset(self):
        return LotQuerySet(self.model, using=self._db)

    def all_in_stock(self):
        return self.get_queryset().all_in_stock_queryset()


class Lot(models.Model):
    number = models.TextField('Número')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Remédio')
    amount = models.IntegerField('Quantidade')
    entry_date = models.DateField('Data de Entrada')
    shelf_life_date = models.DateField('Data de Validade')

    objects = LotManager()

    class Meta:
        ordering = ['entry_date', 'shelf_life_date']

    def current_amount(self):
        return self.amount - (self.bottle_set.count() + self.medicine.freesample_set.count())

    def __str__(self):
        return "{}".format(self.number)


class FreeSample(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Medicamento')
    date = models.DateField('Data', default=timezone.now())

    def __str__(self):
        return "{} - {}".format(self.medicine.name, self.patient.name)
