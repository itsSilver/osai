from django.urls import path
from mail.views import send_to_user_email

app_name = 'mail'

urlpatterns = [
    path("send_mail", send_to_user_email)
]
