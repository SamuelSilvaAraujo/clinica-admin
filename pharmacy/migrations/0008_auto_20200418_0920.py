# Generated by Django 2.2.7 on 2020-04-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_auto_20200313_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='volume',
            field=models.CharField(max_length=10, verbose_name='Volume'),
        ),
    ]