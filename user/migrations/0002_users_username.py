# Generated by Django 4.0.4 on 2022-05-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]