# Generated by Django 2.2.7 on 2020-06-02 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0008_auto_20200418_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='number',
        ),
    ]