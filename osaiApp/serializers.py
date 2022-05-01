from django.contrib.auth.models import User
from rest_framework import serializers

from osaiApp.models import Ocorenze


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class OcorenzeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocorenze
        fields = ['name', 'description']
