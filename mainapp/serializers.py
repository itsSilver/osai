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

    class Meta:
        model = Segnalazioni

        fields = ("id","titolo","note", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina","rif_ticket", "id_stato_segnalazione","immagine_1","immagine_2","immagine_3")


class SegnalazioniSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    descrizione = serializers.CharField()
    id_allarme = serializers.CharField(max_length=255)
    descrizione_allarme = serializers.CharField()
    famiglia_macchina = serializers.CharField(max_length=255)
    sottofamiglia_macchina = serializers.CharField(max_length=255)
    id_stato_segnalazione = serializers.CharField(
        allow_blank=True, required=False)
    rif_ticket = serializers.CharField(max_length=255)

    class Meta:
        model = Segnalazioni

        fields = ("titolo", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina", "id_stato_segnalazione","id","created_at","updated_at","rif_ticket")

    def create(self, validated_data):
        """
        Create and return a new `Segnalazioni` instance, given the validated data.
        """
        return SegnalazioniSerializer.objects.create(**validated_data)


class SoluzioniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soluzioni

        fields = ("rif_ticket","occorrenze", "titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione","id","created_at","updated_at","rif_ticket")

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Soluzioni` instance, given the validated data.
    #     """
    #     return SoluzioniSerializer.objects.create(**validated_data)


class OccorrenzeDisplaySerializer(serializers.ModelSerializer):
    # segnalazione = SegnalazioniDisplaySerializer(read_only=True)

    class Meta:
        model = Occorrenze

        fields = ("id","segnalazione", "titolo", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza", "note", "stato_occorrenza","id","created_at","updated_at","rif_ticket")


class SoluzioniDisplaySerializer(serializers.ModelSerializer):
    id_stato_soluzione = StatiSoluzioneSerializer(required=False)
    occorrenze = OccorrenzeDisplaySerializer(required=False)

    class Meta:
        model = Soluzioni

        fields = ("id","occorrenze", "titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione")


class OccorrenzeSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(max_length=255)
    descrizione = serializers.CharField()
    commessa_macchina = serializers.CharField(max_length=255)
    versione_sw_1 = serializers.CharField(max_length=255)
    versione_sw_2 = serializers.CharField(max_length=255)
    data_occorrenza = serializers.CharField(max_length=255)
    stato_occorrenza = serializers.IntegerField()
    note = serializers.CharField()
    rif_ticket = serializers.CharField(max_length=255)
    class Meta:
        model = Occorrenze

        fields = ("rif_ticket","titolo", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza", "note", "stato_occorrenza")

    def create(self, validated_data):
        """
        Create and return a new `Soluzioni` instance, given the validated data.
        """
        return OccorrenzeSerializer.objects.create(**validated_data)
