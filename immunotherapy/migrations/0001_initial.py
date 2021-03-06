# Generated by Django 2.2.7 on 2019-12-03 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immunotherapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('total', models.IntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('status', models.CharField(choices=[('using', 'Usando'), ('used', 'usado')], max_length=15)),
                ('immunotherapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immunotherapy.Immunotherapy')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Lot')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('applicator', models.CharField(max_length=50, verbose_name='Aplicador')),
                ('dosage', models.FloatField(verbose_name='Dosagem')),
                ('bottle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immunotherapy.Bottle')),
            ],
        ),
    ]
