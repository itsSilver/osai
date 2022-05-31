# Generated by Django 4.0.4 on 2022-05-31 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_soluzioni_occorrenze'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occorrenze',
            name='segnalazione',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.segnalazioni'),
        ),
        migrations.AlterField(
            model_name='occorrenze',
            name='titolo',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='segnalazioni',
            name='descrizione',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='segnalazioni',
            name='descrizione_allarme',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='segnalazioni',
            name='famiglia_macchina',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segnalazioni',
            name='note',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segnalazioni',
            name='titolo',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='soluzioni',
            name='titolo',
            field=models.CharField(default=None, max_length=255),
        ),
    ]