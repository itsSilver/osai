# Generated by Django 4.0.4 on 2022-05-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_occorrenze_soluzione_soluzioni_occorrenze'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occorrenze',
            name='segnalazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.segnalazioni'),
        ),
    ]
