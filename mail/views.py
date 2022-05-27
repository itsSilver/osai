from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.renderers import JSONRenderer
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import json


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_to_user_email(request):
    send_mail(
        subject='A cool subject',
        message='A stunning message',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS]
    )
    return JsonResponse({"Status": 200, "Message": "Success"}, safe=False)


