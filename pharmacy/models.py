from django.db import models


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
    category = models.ForeignKey(MedicineCategory, on_delete=models.SET_NULL, null=True)
    illness = models.ManyToManyField(Illness, verbose_name='Doenças', blank=True)
    composition = models.TextField('Composição')
    volume = models.FloatField('Volume')


class Lot(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Remédio')
    amount = models.IntegerField('Quantidade')
    entry_date = models.DateField('Data de Entrada')
    shelf_life_date = models.DateField('Data de Validade')
    number = models.IntegerField('Número')
