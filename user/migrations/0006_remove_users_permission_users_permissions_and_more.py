# Generated by Django 4.0.4 on 2022-05-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0005_userhaspermissions_remove_modelhasroles_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='permission',
        ),
        migrations.AddField(
            model_name='users',
            name='permissions',
            field=models.ManyToManyField(related_name='user_permissions', to='auth.permission'),
        ),
        migrations.DeleteModel(
            name='UserHasPermissions',
        ),
    ]