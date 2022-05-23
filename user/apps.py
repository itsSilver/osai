from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        from user.models import Users
        users, created = Users.objects.get_or_create(name="admin", username="admin", email="admin@live.com",
                                                     is_admin=True, is_superuser=True,
                                                     password="admin12345", is_active=True)


