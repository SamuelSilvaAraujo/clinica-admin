# Generated by Django 2.2.7 on 2019-12-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immunotherapy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottle',
            old_name='number',
            new_name='bottle_number',
        ),
        migrations.RenameField(
            model_name='bottle',
            old_name='lote',
            new_name='lot',
        ),
        migrations.RenameField(
            model_name='immunotherapy',
            old_name='total',
            new_name='total_applications',
        ),
        migrations.AddField(
            model_name='immunotherapy',
            name='status',
            field=models.CharField(choices=[('finished', 'Finalizado'), ('in-progress', 'Em Andamento')], default='finished', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='status',
            field=models.CharField(choices=[('in-use', 'Em uso'), ('used', 'usado')], max_length=15),
        ),
    ]
