# Generated by Django 4.0.4 on 2022-06-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_users_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
