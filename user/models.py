from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser, Permission
from django.db import models


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=self.normalize_email(name),
            username=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)


class Users(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=255, unique=True, default=None)
    email = models.EmailField(verbose_name="email",
                              max_length=60, unique=True, default=None)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    permissions = models.ManyToManyField(
        Permission, 'user_permissions')

    USERNAME_FIELD = 'email'

    EMAIL_FIELD = "email"

    objects = MyAccountManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser

# class Roles(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     guard_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         db_table = 'roles'


# class ModelHasRoles(models.Model):
#     role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
#     model_type = models.CharField(max_length=255)
#     model_id = models.PositiveBigIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'model_has_roles'
#         unique_together = (('role', 'model_id', 'model_type'),)


# class RoleHasPermissions(models.Model):
#     permission = models.OneToOneField(
#         Permissions, models.DO_NOTHING, primary_key=True)
#     role = models.ForeignKey('Roles', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'role_has_permissions'
#         unique_together = (('permission', 'role'),)
