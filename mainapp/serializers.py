import json

from rest_framework import serializers
from django.utils.translation import gettext as _

from mainapp.models import Segnalazioni, Soluzioni, Occorrenze, Stati_Soluzione, Stati_Segnalazione


class StatiSoluzioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stati_Soluzione

        fields = ("stato_soluzione", "note")


class StatiSegnalazioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stati_Segnalazione

        fields = ("stato_segnalazione", "note")


class SegnalazioniDisplaySerializer(serializers.ModelSerializer):
    id_stato_segnalazione = StatiSegnalazioneSerializer(required=False)
    immagine_1 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    immagine_2 = serializers.ImageField(
        allow_null=True, max_length=None, required=False)
    immagine_3 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    titolo = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    descrizione = serializers.CharField(required=False, allow_blank=True)
    id_allarme = serializers.CharField(
        required=True, allow_blank=True, max_length=255)
    descrizione_allarme = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    famiglia_macchina = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    sottofamiglia_macchina = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    rif_ticket = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    note = serializers.CharField(
        required=False, allow_blank=True, max_length=255)

    class Meta:
        model = Segnalazioni

        fields = ("id", "created_at", "updated_at", "titolo", "note", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina", "rif_ticket", "id_stato_segnalazione", "immagine_1", "immagine_2", "immagine_3", "user_id")


class SegnalazioniSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    descrizione = serializers.CharField(required=False, allow_blank=True)
    id_allarme = serializers.CharField(max_length=255, required=True)
    descrizione_allarme = serializers.CharField(
        required=False, allow_blank=True)
    famiglia_macchina = serializers.CharField(
        max_length=255, required=False, allow_blank=True)
    sottofamiglia_macchina = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    id_stato_segnalazione = serializers.CharField(
        allow_blank=True, required=False)
    rif_ticket = serializers.CharField(
        required=False, allow_blank=True, max_length=255)
    note = serializers.CharField(
        required=False, allow_blank=True, max_length=255)

    class Meta:
        model = Segnalazioni

        fields = ("titolo", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina", "note", "id_stato_segnalazione", "id", "created_at", "updated_at", "rif_ticket", "user_id")

    def create(self, validated_data):
        """
        Create and return a new `Segnalazioni` instance, given the validated data.
        """
        return SegnalazioniSerializer.objects.create(**validated_data)


class SoluzioniSerializer(serializers.ModelSerializer):
    id_stato_soluzione = StatiSoluzioneSerializer(required=False)

    immagine_1 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    immagine_2 = serializers.ImageField(
        allow_null=True, max_length=None, required=False)
    immagine_3 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    titolo = serializers.CharField(
        required=True, allow_blank=True, max_length=100)
    rank = serializers.IntegerField(required=False)
    descrizione = serializers.CharField(required=False, allow_blank=True)
    settore_riferimento = serializers.CharField(
        required=False, allow_blank=True)
    note = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Soluzioni

        fields = ("rif_ticket", "titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione", "id", "created_at", "updated_at", "rif_ticket", "user_id")

    def create(self, validated_data):
        """
        Create and return a new `Soluzioni` instance, given the validated data.
        """
        return SoluzioniSerializer.objects.create(**validated_data)


class SoluzioniForOcc(serializers.ModelSerializer):
    id_stato_soluzione = StatiSoluzioneSerializer(required=False)

    class Meta:
        model = Soluzioni

        fields = ("id", "titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione", "created_at", "updated_at")


class OccorrenzeDisplaySerializer(serializers.ModelSerializer):
    # segnalazione = SegnalazioniDisplaySerializer(read_only=True)
    # soluzioni = SoluzioniForOcc(many=True, read_only=True, required=False)
    # soluzioni_id = serializers.SerializerMethodField('sol_if')
    descrizione = serializers.CharField(required=False, allow_blank=True)
    commessa_macchina = serializers.CharField(required=False, allow_blank=True)
    titolo = serializers.CharField(required=False, allow_blank=True)
    versione_sw_1 = serializers.CharField(required=False, allow_blank=True)
    versione_sw_2 = serializers.CharField(required=False, allow_blank=True)
    note = serializers.CharField(required=False, allow_blank=True)
    data_occorrenza = serializers.CharField(required=False, allow_blank=True)
    stato_occorrenza = serializers.CharField(required=False, allow_blank=True)
    soluzione = serializers.IntegerField(required=False)

    class Meta:
        model = Occorrenze

        fields = ("id", "segnalazione",   "titolo", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza", "note",  "stato_occorrenza", "id", "created_at", "updated_at", "rif_ticket", "user_id", "soluzione")

    # def sol_if(self, obj):

    #     prof_obj = Soluzioni.objects.filter(occorrenze_id=obj.id)
    #     ids = {}
    #     for id in prof_obj:
    #         ids['id'] = id.id
    #         ids['titolo'] = id.titolo

    #     return ids


class OccorrenzeSignalSerializer(serializers.ModelSerializer):
    # segnalazione = SegnalazioniDisplaySerializer(read_only=True)
    total = serializers.SerializerMethodField('total')

    class Meta:
        model = Occorrenze

        fields = ("total")


class SoluzioniDisplaySerializer(serializers.ModelSerializer):
    id_stato_soluzione = StatiSoluzioneSerializer(required=False)
    # occorrenze = OccorrenzeDisplaySerializer(required=False)

    immagine_1 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    immagine_2 = serializers.ImageField(
        allow_null=True, max_length=None, required=False)
    immagine_3 = serializers.ImageField(
        max_length=None, required=False, allow_null=True)
    titolo = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    rank = serializers.IntegerField(required=False)
    descrizione = serializers.CharField(required=False, allow_blank=True)
    settore_riferimento = serializers.CharField(
        required=False, allow_blank=True)
    note = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Soluzioni
        # fields = '__all__'

        fields = ("id", "titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione", "created_at", "updated_at", "user_id")


class OccorrenzeSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(max_length=255, required=True)
    descrizione = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    commessa_macchina = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True)
    versione_sw_1 = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True)
    versione_sw_2 = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True)
    data_occorrenza = serializers.CharField(max_length=255)
    stato_occorrenza = serializers.IntegerField(required=False)
    note = serializers.CharField(
        required=False, allow_blank=True, allow_null=True)
    rif_ticket = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True)
    soluzione = serializers.IntegerField(required=False)

    class Meta:
        model = Occorrenze

        fields = ("rif_ticket", "titolo", "segnalazione", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza", "note", "stato_occorrenza", "soluzione")

    def create(self, validated_data):
        """
        Create and return a new `Soluzioni` instance, given the validated data.
        """
        return OccorrenzeSerializer.objects.create(**validated_data)
