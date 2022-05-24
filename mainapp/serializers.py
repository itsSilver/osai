from rest_framework import serializers

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

        fields = ("titolo", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina", "rif_ticket","id_stato_segnalazione","created_at","updated_at")


class SegnalazioniSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    descrizione = serializers.CharField()
    id_allarme = serializers.CharField(max_length=255)
    descrizione_allarme = serializers.CharField()
    famiglia_macchina = serializers.CharField(max_length=255)
    sottofamiglia_macchina = serializers.CharField(max_length=255)
    rif_ticket = serializers.CharField(max_length=255)
    id_stato_segnalazione = serializers.CharField(
        allow_blank=True, required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Segnalazioni

        fields = ("titolo", "descrizione", "id_allarme", "descrizione_allarme",
                  "famiglia_macchina", "sottofamiglia_macchina","rif_ticket", "id_stato_segnalazione","created_at","updated_at")

    def create(self, validated_data):
        """
        Create and return a new `Segnalazioni` instance, given the validated data.
        """
        return SegnalazioniSerializer.objects.create(**validated_data)


class SoluzioniDisplaySerializer(serializers.ModelSerializer):
    id_stato_soluzione = StatiSoluzioneSerializer(required=False)

    class Meta:
        model = Soluzioni

        fields = ("titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione","created_at","updated_at")


class SoluzioniSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    rank = serializers.IntegerField()
    descrizione = serializers.CharField()
    immagine_1 = serializers.CharField()
    immagine_2 = serializers.CharField()
    immagine_3 = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    settore_riferimento = serializers.CharField(max_length=255)
    note = serializers.CharField()
    id_stato_soluzione = serializers.CharField(
        allow_blank=True, required=False)

    class Meta:
        model = Soluzioni

        fields = ("titolo", "rank", "descrizione", "immagine_1",
                  "immagine_2", "immagine_3", "settore_riferimento", "note", "id_stato_soluzione","created_at","updated_at")

    def create(self, validated_data):
        """
        Create and return a new `Soluzioni` instance, given the validated data.
        """
        return SoluzioniSerializer.objects.create(**validated_data)


class OccorrenzeDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Occorrenze

        fields = ("segnalazione", "soluzione", "titolo", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza","rif_ticket", "note", "stato_occorrenza","created_at","updated_at")


class OccorrenzeSerializer(serializers.ModelSerializer):
    titolo = serializers.CharField(max_length=255)
    descrizione = serializers.CharField()
    commessa_macchina = serializers.CharField(max_length=255)
    versione_sw_1 = serializers.CharField(max_length=255)
    versione_sw_2 = serializers.CharField(max_length=255)
    data_occorrenza = serializers.CharField(max_length=255)
    stato_occorrenza = serializers.IntegerField()
    note = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    rif_ticket = serializers.CharField(max_length=255)

    class Meta:
        model = Occorrenze

        fields = ("segnalazione", "soluzione", "titolo", "descrizione", "commessa_macchina",
                  "versione_sw_1", "versione_sw_2", "data_occorrenza","rif_ticket",  "note", "stato_occorrenza","created_at","updated_at")

    def create(self, validated_data):
        """
        Create and return a new `Soluzioni` instance, given the validated data.
        """
        return OccorrenzeSerializer.objects.create(**validated_data)
