from email.policy import default
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User, Permission
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


# class LoginSerializers(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(
#         label=_("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         max_length=128,
#         write_only=True
#     )

#     def validate(self, data):
#         username = data.get('email')
#         password = data.get('password')

#         if username and password:
#             user = login(request=self.context.get('request'),
#                          username=username, password=password)
#             if not user:
#                 msg = _('Unable to log in with provided credentials.')
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = _('Must include "username" and "password".')
#             raise serializers.ValidationError(msg, code='authorization')

#         data['user'] = user
#         return data


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
    user_permissions = PermissionsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created_at',
                  'updated_at', 'is_admin', 'is_active', 'is_superuser', 'user_permissions')
