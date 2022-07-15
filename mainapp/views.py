from email import message
import re
import os
from django.shortcuts import get_object_or_404, render
from rest_framework.renderers import JSONRenderer
from rest_framework import filters
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
from django.http import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound, ValidationError, ParseError, PermissionDenied

from mainapp.decorators.is_admin import is_admin
from mainapp.models import Segnalazioni, Soluzioni, Occorrenze, Stati_Segnalazione, Stati_Soluzione

from mainapp.serializers import OccorrenzeDisplaySerializer, OccorrenzeSignalSerializer, SegnalazioniDisplaySerializer,  \
    SegnalazioniSerializer, SoluzioniDisplaySerializer, SoluzioniSerializer, OccorrenzeSerializer,  \
    StatiSegnalazioneSerializer, StatiSoluzioneSerializer
from user.models import Users

import json


def __check_if_has_permission(request, permission):
    if request.user.is_admin:
        return True
    if permission in request.user.permissions.values_list('codename', flat=True):
        return True
    else:
        return False


def __format_error_response(errors):
    list_of_errors = []
    for x in errors.keys():
        val = str(x + ": " + str(errors[x][0]))
        list_of_errors.append(val)
    return list_of_errors


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_soluzioni(request):
    """
    It takes a request, validates it, and creates a new Soluzioni object

    :param request: The request object
    :return: The data is being returned as a dictionary.
    """
    check_permission = __check_if_has_permission(request, "add_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to create Soluzioni"})

    try:
        data = {}
        stati = None
        if "stato_soluzione" in request.data:
            stati_serializer = StatiSoluzioneSerializer(
                request.data["stato_soluzione"])

            stati = Stati_Soluzione.objects.create(
                stato_soluzione=stati_serializer.data["stato_soluzione"],
                note=stati_serializer.data["note"]
            )
            stati.save()
        occ = None
        serializer = SoluzioniSerializer(
            data=request.data)
        if serializer.is_valid():
            soluzioni = Soluzioni.objects.create(
                titolo=serializer.data["titolo"],
                rank=serializer.data["rank"] if "rank" in serializer.data else 0,
                descrizione=serializer.data["descrizione"] if "descrizione" in serializer.data else '',
                immagine_1=request.data["immagine_1"] if "immagine_1" in request.data else "",
                immagine_2=request.data["immagine_2"] if "immagine_2" in request.data else "",
                immagine_3=request.data["immagine_3"] if "immagine_3" in request.data else "",
                settore_riferimento=serializer.data["settore_riferimento"] if "settore_riferimento" in serializer.data else '',
                note=serializer.data["note"] if "note" in serializer.data else '',
                id_stato_soluzione=stati,
                user_id=request.user.id
            )

            soluzioni.save()

            data["message"] = "Soluzioni Created successfully"
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_segnalazioni(request):
    """
    It creates a new Segnalazioni object, and saves it to the database.

    :param request: The request object
    :return: The data is being returned as a response.
    """
    check_permission = __check_if_has_permission(request, "add_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to create Segnalazioni"})
    try:
        data = {}
        stati = None
        if "stati_segnalazione" in request.data:
            stati_serializer = StatiSegnalazioneSerializer(
                request.data["stati_segnalazione"])

            stati = Stati_Segnalazione.objects.create(
                stato_segnalazione=stati_serializer.data["stato_segnalazione"],
                note=stati_serializer.data["note"]
            )
            stati.save()

        serializer = SegnalazioniSerializer(
            data=request.data)
        if serializer.is_valid():
            segnalazioni = Segnalazioni.objects.create(
                titolo=serializer.data["titolo"],
                descrizione=serializer.data["descrizione"] if "descrizione" in serializer.data else '',
                id_allarme=serializer.data["id_allarme"] if "id_allarme" in serializer.data else '',
                descrizione_allarme=serializer.data["descrizione_allarme"] if "descrizione_allarme" in serializer.data else '',
                famiglia_macchina=serializer.data["famiglia_macchina"] if "famiglia_macchina" in serializer.data else '',
                sottofamiglia_macchina=serializer.data[
                    "sottofamiglia_macchina"] if "sottofamiglia_macchina" in serializer.data else '',
                immagine_1=request.data["immagine_1"] if "immagine_1" in request.data else "",
                immagine_2=request.data["immagine_2"] if "immagine_2" in request.data else "",
                immagine_3=request.data["immagine_3"] if "immagine_3" in request.data else "",
                id_stato_segnalazione=stati,
                user_id=request.user.id,
                note=serializer.data["note"] if "note" in serializer.data else '',
                rif_ticket=serializer.data["rif_ticket"] if "rif_ticket" in serializer.data else '',

            )

            segnalazioni.save()

            data["message"] = "Segnalazioni Created successfully"
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})

# Soluzioni Occorrenze


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_occorrenze(request):
    """
    It takes a request, validates it, and saves it to the database.

    :param request: The request object
    :return: The data is being returned as a dictionary.
    """
    check_permission = __check_if_has_permission(request, "add_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to Create Occurrenze"})
    try:
        check = Segnalazioni.objects.get(id=request.data['segnalazione'])
    except Exception:
        res = {}
        res['message'] = "Segnalazioni Not Found"
        res['code'] = 400
        raise ValidationError(res)

    try:
        data = {}
        serializer = OccorrenzeSerializer(
            data=request.data)
        if serializer.is_valid():

            if not "segnalazione" in request.data:
                res = {}
                res['message'] = "segnalazione_id is missing"
                res['code'] = 400
                raise ValidationError(res)

            if "soluzione" in request.data:
                sol = Soluzioni.objects.filter(pk=request.data['soluzione']).values(
                    'id')
            data["message"] = "Occurrenze Created successfully"
            occorrenze = Occorrenze(
                titolo=serializer.data["titolo"],
                descrizione=serializer.data["descrizione"] if 'descrizione' in serializer.data else '',
                rif_ticket=serializer.data["rif_ticket"] if 'rif_ticket' in serializer.data else '',
                commessa_macchina=serializer.data["commessa_macchina"]if 'commessa_macchina' in serializer.data else '',
                versione_sw_1=serializer.data["versione_sw_1"]if 'versione_sw_1' in serializer.data else '',
                versione_sw_2=serializer.data["versione_sw_2"] if 'versione_sw_2' in serializer.data else '',
                data_occorrenza=serializer.data["data_occorrenza"],
                stato_occorrenza=serializer.data["stato_occorrenza"] if 'stato_occorrenza' in serializer.data else 0,
                note=serializer.data["note"] if 'note' in serializer.data else '',
                user_id=request.user.id,
                soluzione=sol if sol else None
            )
            occorrenze.segnalazione_id = request.data["segnalazione"]
            occorrenze.save()
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def retrive_user_segnalazioni(request):
    """
    It takes the user id from the request, then it filters the Segnalazioni model by the user id, then
    it serializes the data and returns it as a JsonResponse.

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Segnalazioni"})

    user_segnalazioni = Segnalazioni.objects.all(
    ).prefetch_related('id_stato_segnalazione')
    serializer_class = SegnalazioniDisplaySerializer(
        user_segnalazioni, many=True).data
    newResponse = []
    for segnal in serializer_class:
        total = Occorrenze.objects.raw(
            'SELECT COUNT(*) as id FROM defaultdb.occorrenze WHERE segnalazione_id = %s', [segnal['id']])[:][0].id
        segnal['total_occorrenze'] = total
        name = Users.objects.get(pk=segnal['user_id'])
        user = str(name)
        segnal['username'] = user
        newResponse.append(segnal)

    return JsonResponse(newResponse, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_segnalazioni_by_id(request, id):

    check_permission = __check_if_has_permission(request, "view_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Segnalazioni"})
    user_segnalazioni = Segnalazioni.objects.filter(
        pk=id).prefetch_related('id_stato_segnalazione')
    if user_segnalazioni[0].user.id == request.user.id or user_segnalazioni[0].user.is_admin:
        serializer_class = SegnalazioniDisplaySerializer(
            user_segnalazioni, many=True).data
        return JsonResponse(serializer_class, safe=False)
    else:
        raise NotFound("Segnalazioni not found")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrive_all_segnalazioni(request):
    """
    It takes a request, gets all the objects from the Segnalazioni model, serializes them and returns
    them as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Segnalazioni"})
    queryset = Segnalazioni.objects.all().prefetch_related('id_stato_segnalazione')
    serializer_class = SegnalazioniDisplaySerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_segnalazioni(request, id):
    """
    It takes the id of the segnalazioni object and deletes it from the database

    :param request: The request object
    :param id: The id of the segnalazioni you want to remove
    :return: The response is a string.
    """
    check_permission = __check_if_has_permission(
        request, "delete_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to remove Segnalazioni"})

    segnalazioni = get_object_or_404(Segnalazioni, pk=id)
    if(segnalazioni.user_id == request.user.id or request.user.is_superuser == True):
        segnalazioni.delete()
        return JsonResponse({"status": 200, "message": "Segnalazioni Removed successfully"})
    raise NotFound("Segnalazioni not found")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_segnalazioni_image_1(request, id):
    check_permission = __check_if_has_permission(
        request, "change_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Segnalazioni"})
    seg = get_object_or_404(Segnalazioni, pk=id)

    old_img = seg.immagine_1
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Segnalazioni.objects.filter(pk=id).update(immagine_1=None)

    return JsonResponse('Image 1 removed succesfully', status=200, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_segnalazioni_image_2(request, id):
    check_permission = __check_if_has_permission(
        request, "change_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Segnalazioni"})
    seg = get_object_or_404(Segnalazioni, pk=id)

    old_img = seg.immagine_2
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Segnalazioni.objects.filter(pk=id).update(immagine_2=None)

    return JsonResponse('Image 2 removed succesfully', status=200, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_segnalazioni_image_3(request, id):
    check_permission = __check_if_has_permission(
        request, "change_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Segnalazioni"})
    seg = get_object_or_404(Segnalazioni, pk=id)

    old_img = seg.immagine_3
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Segnalazioni.objects.filter(pk=id).update(immagine_3=None)

    return JsonResponse('Image 3 removed succesfully', status=200, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_soluzioni_image_1(request, id):
    check_permission = __check_if_has_permission(
        request, "change_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Soluzioni"})
    seg = get_object_or_404(Soluzioni, pk=id)

    old_img = seg.immagine_1
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Soluzioni.objects.filter(pk=id).update(immagine_1=None)

    return JsonResponse('Image 1 removed succesfully', status=200, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_soluzioni_image_2(request, id):
    check_permission = __check_if_has_permission(
        request, "change_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Soluzioni"})
    seg = get_object_or_404(Soluzioni, pk=id)

    old_img = seg.immagine_2
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Soluzioni.objects.filter(pk=id).update(immagine_2=None)

    return JsonResponse('Image 2 removed succesfully', status=200, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_soluzioni_image_3(request, id):
    check_permission = __check_if_has_permission(
        request, "change_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Soluzioni"})
    seg = get_object_or_404(Soluzioni, pk=id)

    old_img = seg.immagine_3
    print('old_img', old_img)
    if os.path.exists(os.path.join(
            'media/' + str(old_img))):
        os.remove(os.path.join(
            'media/' + str(old_img)))
        Soluzioni.objects.filter(pk=id).update(immagine_3=None)

    return JsonResponse('Image 3 removed succesfully', status=200, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_segnalazioni(request, id):
    """
    If the user is authenticated, get the segnalazioni object with the id passed in the url, if the user
    is the owner of the object, update the object with the data passed in the request.

    :param request: The request object
    :param id: the id of the segnalazioni
    :return: The response is a JSON object with the status and message.
    """
    check_permission = __check_if_has_permission(
        request, "change_segnalazioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to update Segnalazioni"})
    seg = get_object_or_404(Segnalazioni, pk=id)

    if(seg.user_id == request.user.id):
        serializer = SegnalazioniDisplaySerializer(
            instance=seg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
    raise NotFound("Segnalazioni not found")


# Soluzioni Endpoints

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_soluzioni(request, id):
    """
    If the user is authenticated, then get the soluzioni object with the given id, if the soluzioni
    object exists, then check if the user id of the soluzioni object is the same as the user id of the
    user who is making the request, if it is, then delete the soluzioni object and return a JSON
    response with a status of 200 and a message of "Soluzioni Removed successfully", otherwise return a
    JSON response with a status of 404 and a message of "Soluzioni not found"

    :param request: The request object
    :param id: The id of the soluzioni to be deleted
    :return: The response is a JSON object with a status and a message.
    """
    check_permission = __check_if_has_permission(request, "delete_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to remove Soluzioni"})

    soluzioni = get_object_or_404(Soluzioni, pk=id)
    if(soluzioni.user_id == request.user.id or request.user.is_superuser == True):
        soluzioni.delete()
        return JsonResponse({"status": 200, "message": "Soluzioni Removed successfully"})
    raise NotFound("Soluzioni not found")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def retrive_user_soluzioni(request):
    """
    It takes the user id from the request, then it filters the Soluzioni model by the user id, then it
    serializes the data and returns it as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to View Soluzioni"})

    # user_id = request.user.id
    # user_soluzioni = Soluzioni.objects.filter(user=user_id)
    user_soluzioni = Soluzioni.objects.all()
    serializer_class = SoluzioniDisplaySerializer(
        user_soluzioni, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_soluzioni_by_id(request, id):
    check_permission = __check_if_has_permission(request, "view_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Soluzioni"})
    user_soluzioni = Soluzioni.objects.filter(
        pk=id).prefetch_related('id_stato_soluzione')
    serializer_class = SoluzioniDisplaySerializer(
        user_soluzioni, many=True).data
    print(serializer_class)
    return JsonResponse(serializer_class, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_occorrenze_by_se_id(request, id):
    check_permission = __check_if_has_permission(request, "view_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Soluzioni"})
    user_soluzioni = Occorrenze.objects.filter(
        segnalazione=id)
    serializer_class = OccorrenzeDisplaySerializer(
        user_soluzioni, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_soluzioni(request, id):
    """
    If the user is authenticated, and the user id matches the id of the user who created the object,
    then update the object

    :param request: The request object
    :param id: the id of the solution to be updated
    :return: The data that is being returned is the data that is being passed in the request.
    """
    check_permission = __check_if_has_permission(request, "change_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to Update Soluzioni"})
    seg = get_object_or_404(Soluzioni, pk=id)
    if(seg.user_id == request.user.id or request.user.is_superuser == True):
        serializer = SoluzioniDisplaySerializer(
            instance=seg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
    raise NotFound("Soluzioni not found")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrive_all_soluzioni(request):
    """
    It takes a request, gets all the objects from the Soluzioni model, serializes them and returns
    them as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_soluzioni")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to View Soluzioni"})
    queryset = Soluzioni.objects.all()
    serializer_class = SoluzioniDisplaySerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)

# Soluzioni Endpoints


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_occorrenze(request, id):
    """
    If the user is authenticated, and the user is the owner of the occorrenze, then delete the
    occorrenze

    :param request: The request object
    :param id: The id of the occorrenze you want to delete
    :return: The response is a JSON object with two keys: status and message.
    """
    check_permission = __check_if_has_permission(request, "delete_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to Remove Occurrenze"})

    occorrenze = get_object_or_404(Occorrenze, pk=id)
    occorrenze.delete()

    # if(occorrenze.user_id == request.user.id):
    # raise NotFound("Occorrenze not found")
    return JsonResponse({"status": 200, "message": "Occorrenze Removed successfully"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def retrive_user_occurrenze(request):
    """
    It takes the user id from the request, then it filters the Occorrenze model by the user id, then it
    serializes the data and returns it as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to View Occurrenze"})

    user_occurrenze = Occorrenze.objects.all()
    serializer_class = OccorrenzeDisplaySerializer(
        user_occurrenze, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_occurrenze_by_id(request, id):
    check_permission = __check_if_has_permission(request, "view_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to view Occurrenze"})
    user_occurrenze = Occorrenze.objects.filter(pk=id)
    # if user_occurrenze[0].user.id == request.user.id or user_occurrenze[0].user.is_admin:
    serializer_class = OccorrenzeDisplaySerializer(
        user_occurrenze, many=True).data
    return JsonResponse(serializer_class, safe=False)
    # else:
    #     return JsonResponse({"status": 404, "message": "Occurrenze not found"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_occurrenze(request, id):
    """
    If the user is authenticated, get the Occorrenze object with the id passed in the url, if the
    user_id of the Occorrenze object is the same as the user_id of the user that is authenticated, then
    update the Occorrenze object with the data passed in the request

    :param request: The request object
    :param id: the id of the occurrence
    :return: The data is being returned as a JsonResponse.
    """
    check_permission = __check_if_has_permission(request, "change_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to Update Occurrenze"})

    occ = get_object_or_404(Occorrenze, id=id)
    # copy_data = {**request.data}
    # if 'soluzioni_id' not in copy_data:
    #     copy_data['soluzioni_id'] = occ.soluzioni_id
    # try:
    #     check = Segnalazioni.objects.get(id=request.data['segnalazione'])
    # except Exception:
    #     res = {}
    #     res['message'] = "Segnalazioni  Not    Found "
    #     res['code'] = 400
    #     raise ValidationError(res)
    serializer = OccorrenzeDisplaySerializer(
        instance=occ, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        errors = __format_error_response(serializer.errors)
        res = {}
        res['message'] = errors
        res['code'] = 400
        raise ValidationError(res)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def connect_occorrenze_to_segnalazioni(request, id):
    check_permission = __check_if_has_permission(request, "change_occorrenze")

    if not check_permission:
        raise PermissionDenied(
            {"message": "This user do not have permission to Update Occurrenze"})

    if 'segnalazioni_id' not in request.data:
        res = {}
        res["message"] = "segnalazioni_id is missing"
        res['code'] = 400
        raise ValidationError(res)

    if not isinstance(request.data['segnalazioni_id'], int):
        res = {}
        res["message"] = "Field 'segnalazioni_id' expected a number but got String."
        res['code'] = 400
        raise ValidationError(res)

    occ = get_object_or_404(Occorrenze, pk=id)
    seg = get_object_or_404(Segnalazioni, pk=request.data['segnalazioni_id'])

    occ.segnalazione = seg
    occ.save(update_fields=['segnalazione'])
    data = OccorrenzeDisplaySerializer(
        instance=occ, data=occ.__dict__)
    if data.is_valid():
        return JsonResponse(data.data, status=200, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def connect_soluzioni_to_occorrenze(request, id):
    if id:
        check_permission = __check_if_has_permission(
            request, "change_soluzioni")

        if not check_permission:
            raise PermissionDenied(
                {"message": "You do not have permission to Update Soluzioni"})

        if 'occorrenze_id' not in request.data:
            res = {}
            res["message"] = "Field 'occorrenze_id' is missing."
            res['code'] = 400
            raise ValidationError("occorrenze_id is missing")

        if not isinstance(request.data['occorrenze_id'], int):
            res = {}
            res["message"] = "Field 'occorrenze_id' expected a number but got String."
            res['code'] = 400
            raise ValidationError(res)

        sol = get_object_or_404(Soluzioni, pk=id)
        occ = get_object_or_404(Occorrenze, pk=request.data['occorrenze_id'])
        sol.occorrenze = occ
        sol.save(update_fields=['occorrenze'])
    return JsonResponse({"message": "Connected successfully",
                         "status": 200}, status=200, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def disconnect_soluzioni_to_occorrenze(request, id):
    if id:
        check_permission = __check_if_has_permission(
            request, "change_soluzioni")

        if not check_permission:
            raise PermissionDenied(
                {"message": "You do not have permission to Update Soluzioni"})

        sol = get_object_or_404(Soluzioni, pk=id)
        if sol.occorrenze_id == None:
            return JsonResponse({"message": "This solution is not connected to any occorrenze", "status": 200}, safe=False)

        sol.occorrenze = None
        sol.save(update_fields=['occorrenze'])
    return JsonResponse({"message": "Soluzioni disconnected successfully", "status": 200}, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrive_all_occurrenze(request):
    """
    It takes a request, gets all the objects from the Occorrenze model, serializes them and returns
    them as a JsonResponse

    :param request: The request object
    :return: A list of dictionaries.
    """
    check_permission = __check_if_has_permission(request, "view_occorrenze")
    if not check_permission:
        raise PermissionDenied(
            {"message": "You do not have permission to View Occurrenze"})

    queryset = Occorrenze.objects.all()
    serializer_class = OccorrenzeDisplaySerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrieve_all_stati_soluzioni(request):
    queryset = Stati_Soluzione.objects.all()
    serialize = StatiSoluzioneSerializer(queryset, many=True).data
    return JsonResponse(serialize, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_stati_soluzione(request):
    try:
        serializer = StatiSoluzioneSerializer(request.data)
        if serializer.is_valid():
            occorrenze = Stati_Soluzione(
                stato_soluzione=serializer.data["stato_soluzione"],
                note=serializer.data["note"],
            )
            serializer.save()
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
        return JsonResponse(serializer)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_stati_soluzione(request, id):
    seg = get_object_or_404(Stati_Soluzione, pk=id)
    if(seg.user_id == request.user.id):
        serializer = StatiSoluzioneSerializer(
            instance=seg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data.data, status=200)
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
    raise NotFound("Not found")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_stati_soluzione(request, id):
    stati = get_object_or_404(Stati_Soluzione, pk=id)
    if(stati.user_id == request.user.id or request.user.is_superuser == True):
        stati.delete()
        return JsonResponse({"status": 200, "message": "Stati_Soluzione Removed successfully"})
    raise NotFound("Not found")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_stati_segnalazione(request):
    try:
        serializer = StatiSegnalazioneSerializer(request.data)
        if serializer.is_valid():
            occorrenze = Stati_Segnalazione(
                stato_segnalazione=serializer.data["stato_segnalazione"],
                note=serializer.data["note"],
            )
            serializer.save()
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
        return JsonResponse(serializer)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_stati_segnalazione(request, id):
    seg = get_object_or_404(Stati_Segnalazione, pk=id)
    if(seg.user_id == request.user.id):
        serializer = StatiSegnalazioneSerializer(
            instance=seg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            errors = __format_error_response(serializer.errors)
            res = {}
            res['message'] = errors
            res['code'] = 400
            raise ValidationError(res)
    raise NotFound("Not found")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@is_admin
def retrieve_all_stati_segnalazione(request):
    queryset = Stati_Segnalazione.objects.all()
    serialize = StatiSegnalazioneSerializer(queryset, many=True).data
    return JsonResponse(serialize, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_stati_segnalazione(request, id):
    stati = get_object_or_404(Stati_Segnalazione, pk=id)
    if(stati.user_id == request.user.id or request.user.is_superuser == True):
        stati.delete()
        return JsonResponse({"status": 200, "message": "Stati_Segnalazione Removed successfully"})
    raise NotFound("Not found")


class SoluzioniListView(generics.ListAPIView):
    queryset = Soluzioni.objects.all()
    serializer_class = SoluzioniDisplaySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'titolo', 'rank']
    search_fields = ['titolo', '=rank', 'descrizione']


class SegnalazioneListView(generics.ListAPIView):
    queryset = Segnalazioni.objects.all().prefetch_related('id_stato_segnalazione')
    serializer_class = SegnalazioniDisplaySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['titolo', 'id_allarme', 'descrizione',
                     'descrizione_allarme', 'famiglia_macchina']
    ordering_fields = ['id', 'titolo', 'id_allarme']


class OccorrenzeListView(generics.ListAPIView):
    queryset = Occorrenze.objects.all()
    serializer_class = OccorrenzeDisplaySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['titolo', 'commessa_macchina',
                     'descrizione', 'versione_sw_1', '=stato_occorrenza']
    ordering_fields = ['id', 'titolo', 'commessa_macchina', 'versione_sw_1']
