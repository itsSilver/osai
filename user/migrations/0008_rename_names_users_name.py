# Generated by Django 4.0.4 on 2022-05-23 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_users_name_users_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='names',
            new_name='name',
        ),
    ]
