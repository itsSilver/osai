from email import message
import re
from django.shortcuts import get_object_or_404, render
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
from mainapp.decorators.is_admin import is_admin
from mainapp.models import Segnalazioni, Soluzioni, Occorrenze, Stati_Segnalazione, Stati_Soluzione

from mainapp.serializers import OccorrenzeDisplaySerializer, SegnalazioniDisplaySerializer,  \
    SegnalazioniSerializer, SoluzioniDisplaySerializer, SoluzioniSerializer, OccorrenzeSerializer,  \
    StatiSegnalazioneSerializer, StatiSoluzioneSerializer


def __check_if_has_permission(request, permission):
    if request.user.is_admin:
        return True
    if permission in request.user.permissions.values_list('codename', flat=True):
        return True
    else:
        return False


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_segnalazioni(request):
    """
    It creates a new Segnalazioni object, and saves it to the database.

    :param request: The request object
    :return: The data is being returned as a response.
    """
    check_permission = __check_if_has_permission(request, "add_segnalazioni")
    if not check_permission:
        return JsonResponse({"status": 403, "message": "You do not have permission to create Segnalazioni"})
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
                descrizione=serializer.data["descrizione"],
                id_allarme=serializer.data["id_allarme"],
                descrizione_allarme=serializer.data["descrizione_allarme"],
                famiglia_macchina=serializer.data["famiglia_macchina"],
                sottofamiglia_macchina=serializer.data["sottofamiglia_macchina"],
                id_stato_segnalazione=stati,
                user_id=request.user.id,

            )

            segnalazioni.save()

            data["message"] = "Segnalazioni Created successfully"
        else:
            data = serializer.errors

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(["POST"])
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
        return JsonResponse({"status": 403, "message": "You do not have permission to view Segnalazioni"})

    user_id = request.user.id
    user_segnalazioni = Segnalazioni.objects.filter(
        user=user_id).prefetch_related('id_stato_segnalazione')
    serializer_class = SegnalazioniDisplaySerializer(
        user_segnalazioni, many=True).data
    return JsonResponse(serializer_class, safe=False)


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
        return JsonResponse({"status": 403, "message": "You do not have permission to view Segnalazioni"})
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
        return JsonResponse({"status": 403, "message": "You do not have permission to remove Segnalazioni"})

    segnalazioni = get_object_or_404(Segnalazioni, pk=id)
    if(segnalazioni.user_id == request.user.id):
        segnalazioni.delete()
        return JsonResponse({"status": 200, "message": "Segnalazioni Removed successfully"})
    return JsonResponse({"status": 404, "message": "Segnalazioni not found"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
        return JsonResponse({"status": 403, "message": "You do not have permission to update Segnalazioni"})
    seg = Segnalazioni.objects.get(pk=id)
    if(seg.user_id == request.user.id):
        data = SegnalazioniDisplaySerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "Segnalazioni not found"})
    return JsonResponse({"status": 404, "message": "Segnalazioni not found"})


# Soluzioni Endpoints
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_soluzioni(request):
    """
    It takes a request, validates it, and creates a new Soluzioni object

    :param request: The request object
    :return: The data is being returned as a dictionary.
    """
    #     {
    #     "titolo": "test title",
    #     "rank": 3,
    #     "descrizione": "test allarmante id",
    #     "immagine_1": "test description alarm",
    #     "immagine_2": "test family machine",
    #     "immagine_3": "test test",
    #     "settore_riferimento": "test test",
    #     "note": "test test"
    # }
    check_permission = __check_if_has_permission(request, "add_soluzioni")
    if not check_permission:
        return JsonResponse({"status": 403, "message": "You do not have permission to create Soluzioni"})

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

        serializer = SoluzioniSerializer(
            data=request.data)
        if serializer.is_valid():
            soluzioni = Soluzioni.objects.create(
                titolo=serializer.data["titolo"],
                rank=serializer.data["rank"],
                descrizione=serializer.data["descrizione"],
                immagine_1=serializer.data["immagine_1"],
                immagine_2=serializer.data["immagine_2"],
                immagine_3=serializer.data["immagine_3"],
                settore_riferimento=serializer.data["settore_riferimento"],
                note=serializer.data["note"],
                id_stato_soluzione=stati,
                user_id=request.user.id
            )

            soluzioni.save()

            data["message"] = "Soluzioni Created successfully"
        else:
            data = serializer.errors

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to remove Soluzioni"})

    soluzioni = get_object_or_404(Soluzioni, pk=id)
    if(soluzioni.user_id == request.user.id):
        soluzioni.delete()
        return JsonResponse({"status": 200, "message": "Soluzioni Removed successfully"})
    return JsonResponse({"status": 404, "message": "Soluzioni not found"})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to View Soluzioni"})

    user_id = request.user.id
    user_soluzioni = Soluzioni.objects.filter(user=user_id)
    serializer_class = SoluzioniDisplaySerializer(
        user_soluzioni, many=True).data
    return JsonResponse(serializer_class, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
        return JsonResponse({"status": 403, "message": "You do not have permission to Update Soluzioni"})
    seg = Soluzioni.objects.get(pk=id)
    if(seg.user_id == request.user.id):
        data = SoluzioniDisplaySerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "Soluzioni not found"})
    return JsonResponse({"status": 404, "message": "Soluzioni not found"})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to View Soluzioni"})
    queryset = Soluzioni.objects.all()
    serializer_class = SoluzioniDisplaySerializer(queryset, many=True).data
    return JsonResponse(serializer_class, safe=False)

# Soluzioni Endpoints


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
        return JsonResponse({"status": 403, "message": "You do not have permission to Create Occurrenze"})

    # {
    #     "titolo": "test title",
    #     "descrizione": "test allarmante id",
    #     "commessa_macchina": "test description alarm",
    #     "versione_sw_1": "test family machine",
    #     "versione_sw_2": "test test",
    #     "data_occorrenza": "test test",
    #     "stato_occorrenza": "test test",
    #     "note": "test test"
    # }

    try:
        data = {}
        serializer = OccorrenzeSerializer(
            data=request.data)
        if serializer.is_valid():
            occorrenze = Occorrenze(
                titolo=serializer.data["titolo"],
                descrizione=serializer.data["descrizione"],
                commessa_macchina=serializer.data["commessa_macchina"],
                versione_sw_1=serializer.data["versione_sw_1"],
                versione_sw_2=serializer.data["versione_sw_2"],
                data_occorrenza=serializer.data["data_occorrenza"],
                stato_occorrenza=serializer.data["stato_occorrenza"],
                note=serializer.data["note"],
                user_id=request.user.id
            )
            occorrenze.segnalazione_id = request.data["segnalazione"]
            occorrenze.soluzione_id = request.data["soluzione"]
            occorrenze.save()

            data["message"] = "Soluzioni Created successfully"
        else:
            data = serializer.errors

        return Response(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to Remove Occurrenze"})

    occorrenze = get_object_or_404(Occorrenze, pk=id)
    if(occorrenze.user_id == request.user.id):
        occorrenze.delete()
        return JsonResponse({"status": 200, "message": "Occorrenze Removed successfully"})
    return JsonResponse({"status": 404, "message": "Occorrenze not found"})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to View Occurrenze"})

    user_id = request.user.id
    user_occurrenze = Occorrenze.objects.filter(user=user_id)
    serializer_class = OccorrenzeDisplaySerializer(
        user_occurrenze, many=True).data
    return JsonResponse(serializer_class, safe=False)


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
        return JsonResponse({"status": 403, "message": "You do not have permission to Update Occurrenze"})

    seg = Occorrenze.objects.get(pk=id)
    if(seg.user_id == request.user.id):
        data = OccorrenzeDisplaySerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "Occorrenze not found"})
    return JsonResponse({"status": 404, "message": "Occorrenze not found"})


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
        return JsonResponse({"status": 403, "message": "You do not have permission to View Occurrenze"})

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
        return JsonResponse(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_stati_soluzione(request, id):
    seg = Stati_Soluzione.objects.get(pk=id)
    if(seg.user_id == request.user.id):
        data = StatiSoluzioneSerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "Occorrenze not found"})
    return JsonResponse({"status": 404, "message": "Occorrenze not found"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_stati_soluzione(request, id):
    stati = get_object_or_404(Stati_Soluzione, pk=id)
    if(stati.user_id == request.user.id):
        stati.delete()
        return JsonResponse({"status": 200, "message": "Stati_Soluzione Removed successfully"})
    return JsonResponse({"status": 404, "message": "Stati_Soluzione not found"})


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
        return JsonResponse(data)
    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_stati_segnalazione(request, id):
    seg = Stati_Segnalazione.objects.get(pk=id)
    if(seg.user_id == request.user.id):
        data = StatiSegnalazioneSerializer(
            instance=seg, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=200)
        else:
            return JsonResponse({"status": 200, "message": "Occorrenze not found"})
    return JsonResponse({"status": 404, "message": "Occorrenze not found"})


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
    if(stati.user_id == request.user.id):
        stati.delete()
        return JsonResponse({"status": 200, "message": "Stati_Segnalazione Removed successfully"})
    return JsonResponse({"status": 404, "message": "Stati_Segnalazione not found"})