# Generated by Django 2.2.7 on 2019-12-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.Medicine', verbose_name='Remédio'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='number',
            field=models.TextField(verbose_name='Número'),
        ),
    ]
