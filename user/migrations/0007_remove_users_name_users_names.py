# Generated by Django 4.0.4 on 2022-05-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_users_permission_users_permissions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.AddField(
            model_name='users',
            name='names',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
