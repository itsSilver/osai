from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser, Permission
from django.db import models


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, fullname=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=self.normalize_email(email),
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
    name = models.CharField(max_length=255, unique=True, default=None)
    username = models.CharField(max_length=255, unique=True, default=None)
    email = models.EmailField(verbose_name="email",
                              max_length=60, unique=True, default=None)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
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

