# Generated by Django 2.2.7 on 2020-07-06 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immunotherapy', '0013_auto_20200703_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ('date',)},
        ),
    ]
