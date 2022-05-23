from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()



class RegistrationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(default=email)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    is_admin = serializers.BooleanField(default=0)

    class Meta:
        model = User

        fields = ("name", "email", "password", "is_admin", "username")
        extra_kwargs = {
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'] if type(validated_data['username']) is str else validated_data['email'],
            name=validated_data['name'],
            email=validated_data['email'],
            is_admin=validated_data['is_admin']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name', 'codename')


class UserSerializer(serializers.ModelSerializer):
    permissions = PermissionsSerializer(many=True, source='user_permissions')

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'created_at',
                  'updated_at', 'is_admin', 'is_active', 'is_superuser', 'user_permissions', "permissions")
