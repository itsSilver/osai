from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from mainapp.decorators.is_admin import is_admin
from user.models import Users
from user.serializers import RegistrationSerializer, UserSerializer, PermissionsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError, ParseError

from user.models import Users
from user.serializers import RegistrationSerializer, UserSerializer, PermissionsSerializer

User = get_user_model()


@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True

            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token
            data["id"] account.id

        else:
            data = serializer.errors

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    data = {}
    reqBody = request.data
    email1 = reqBody['email']
    password = reqBody['password']
    try:

        Account = User.objects.get(email=email1)
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})

    token = Token.objects.get_or_create(user=Account)[0].key
    if not check_password(password, Account.password):
        raise ValidationError({"message": "Incorrect Login credentials"})

    if Account:
        if Account.is_active:
            login(request, Account)
            data["message"] = "user logged in"
            data["email"] = Account.email

            Res = {"data": data, "token": token}

            return Response(Res)

        else:
            raise ValidationError({"400": f'Account not active'})

    else:
        raise ValidationError({"400": f'Account doesnt exist'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@is_admin
def user_delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return JsonResponse({"status": 200, "message": "User Removed successfully"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_user(request, id):
    seg = get_object_or_404(User, pk=id)
    if(seg.id == request.user.id):
        data = UserSerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "User not found"})
    raise NotFound("User not found")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@is_admin
def add_permission_to_user(request, id):
    user = get_object_or_404(User, pk=id)
    permissions = request.data["permission_id"]
    for per in permissions:
        user.permissions.add(per)
        user.save()
    if user:
        return JsonResponse({"status": 200, "message": "User permission updated successfully"})
    else:
        raise NotFound("User not found")


@ api_view(["GET"])
@ permission_classes([IsAuthenticated])
@ is_admin
def get_users(request):
    queryset = Users.objects.all()
    serializer_class = UserSerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)


@ api_view(['GET'])
@ permission_classes([IsAuthenticated])
def user_detail(request):
    user = User.objects.get(pk=request.user.pk)
    user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data)


@ api_view(['GET'])
@ permission_classes([IsAuthenticated])
def user_by_id(request,id):
    user = User.objects.get(id=id)
    user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data)

@ api_view(['GET'])
@ permission_classes([AllowAny])
@ is_admin
def permissions_list(request):
    permissions = Permission.objects.all()
    permissions_serializer = PermissionsSerializer(permissions, many=True)
    return JsonResponse(permissions_serializer.data, safe=False)


@ api_view(["POST"])
@ permission_classes([IsAuthenticated])
@ is_admin
def add_permission(request, id):
    permissions = request.data['permissions']

    u = User.objects.get(id=id)
    permission_to_add = Permission.objects.filter(codename__in=permissions)
    for permission in permission_to_add:
        u.user_permissions.add(permission)
    return Response({"200": f'Added'})


@ api_view(["POST"])
@ permission_classes([IsAuthenticated])
@ is_admin
def remove_permission(request, id):
    permissions = request.data['permissions']
    u = get_object_or_404(User, pk=id)
    permission_to_add = Permission.objects.filter(codename__in=permissions)
    for permission in permission_to_add:
        u.user_permissions.remove(permission)
    return Response({"200": f'Removed'})

    # return JsonResponse(serializer, safe=False)


@ api_view(["GET"])
@ permission_classes([IsAuthenticated])
def get_segnalazioni(request):
    if not request.user.is_admin:
        if not 'mainapp.view_segnalazioni' in request.user.get_all_permissions():
            return Response({"400": f'Missing Permission'})
    return Response({"200": f'Show info'})


#
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_segnalazioni(request):
#     if not request.user.is_admin:
#         #kur ben migrate modelin dalin keto add/view/change/delete per cdo model...
#         #duhet nje menyre qe te fshijme permissions qe mer user-i kur krijohet dhe 2 endpoint add/remove permission
#         if not request.user.has_permission('view_segnalizioni'):
#             print("# permission error")
#     print(" #display  segnalizioni")
#


@ api_view(["POST"])
@ permission_classes([IsAuthenticated])
@ is_admin
def create_permission(request):
    serializer = PermissionsSerializer(data=request.data)
    if serializer.is_valid():
        per = serializer.save()
        per.save()
        return JsonResponse(per, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrieve_user_by_id(request):
    if 'user_id' not in request.data:
        raise ParseError("User id is missing")
    queryset = get_object_or_404(User, pk=request.data["user_id"])
    serializer_class = UserSerializer(queryset).data
    return JsonResponse(serializer_class, safe=False)
