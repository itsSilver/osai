from django.db import models

from user.models import Users


class Stati_Segnalazione(models.Model):
    id_stato_segnalazione = models.AutoField(primary_key=True)
    stato_segnalazione = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stato_segnalazioni'


class Stati_Soluzione(models.Model):
    id_stato_soluzione = models.AutoField(primary_key=True)
    stato_soluzione = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stato_soluzioni'


def upload_to(instance, filename):
    return f'images/{instance.__class__._meta.model_name}/{filename}'


class Segnalazioni(models.Model):
    id = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=255, blank=True, null=True)
    descrizione = models.TextField()
    id_allarme = models.CharField(max_length=255)
    descrizione_allarme = models.TextField()
    famiglia_macchina = models.CharField(max_length=255)
    rif_ticket = models.CharField(max_length=255,blank=True,null=True)
    immagine_1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    immagine_2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    immagine_3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    sottofamiglia_macchina = models.CharField(max_length=255)
    user = models.ForeignKey(Users, models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    id_stato_segnalazione = models.ForeignKey(
        Stati_Segnalazione, models.CASCADE, db_column='id_stato_segnalazione', blank=True, null=True)

    class Meta:
        db_table = 'segnalazioni'


class Soluzioni(models.Model):
    id = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField()
    descrizione = models.TextField()
    rif_ticket = models.CharField(max_length=255,blank=True,null=True)
    immagine_1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    immagine_2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    immagine_3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    settore_riferimento = models.CharField(max_length=255)
    note = models.TextField()
    occorrenze = models.ForeignKey(
        "Occorrenze", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    id_stato_soluzione = models.ForeignKey(
        Stati_Soluzione, models.DO_NOTHING, db_column='id_stato_soluzione', blank=True, null=True)

    class Meta:
        db_table = 'soluzioni'


class Occorrenze(models.Model):
    id = models.AutoField(primary_key=True)
    titolo = models.CharField(max_length=255)
    descrizione = models.TextField()
    commessa_macchina = models.CharField(max_length=255)
    versione_sw_1 = models.CharField(max_length=255)
    versione_sw_2 = models.CharField(max_length=255)
    data_occorrenza = models.CharField(max_length=255)
    stato_occorrenza = models.IntegerField()
    rif_ticket = models.CharField(max_length=255,blank=True,null=True)
    note = models.TextField()
    user = models.ForeignKey(Users, models.DO_NOTHING)
    segnalazione = models.ForeignKey(
        "Segnalazioni", on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'occorrenze'
