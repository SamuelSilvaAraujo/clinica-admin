from django.db import models


class MedicineCategory(models.Model):
    name = models.CharField('Categoria', max_length=50)


class MedicineApplication(models.Model):
    name = models.CharField('Aplicação', max_length=100)


class Medicine(models.Model):
    name = models.CharField('Remédio', max_length=100)
    category = models.ForeignKey(MedicineCategory, on_delete=models.SET_NULL, null=True)
    application = models.ForeignKey(MedicineApplication, on_delete=models.SET_NULL, null=True)
    composition = models.TextField('Composição')
    volume = models.FloatField('Volume')


class Lote(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.IntegerField('Quantidade')
    entry_date = models.DateField('Data de Entrada')
    shelf_life_date = models.DateField('Data de Validade')
    number = models.IntegerField('Número')
