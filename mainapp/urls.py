from django.urls import path
from mainapp.views import create_segnalazioni, create_soluzioni, \
    create_occorrenze, remove_segnalazioni, remove_soluzioni, remove_occorrenze, \
    retrive_all_occurrenze, retrive_all_soluzioni, retrive_user_occurrenze, \
    retrive_user_segnalazioni, retrive_all_segnalazioni, retrive_user_soluzioni, \
    update_occurrenze, update_segnalazioni, update_soluzioni, create_stati_soluzione, \
    update_stati_soluzione, remove_stati_soluzione, retrieve_all_stati_soluzioni, create_stati_segnalazione, \
    update_stati_segnalazione, remove_stati_segnalazione, retrieve_all_stati_segnalazione

app_name = 'mainapp'

urlpatterns = [
    path("segnalazioni/create", create_segnalazioni),
    path("segnalazioni/retrive_segnalazioni", retrive_user_segnalazioni),
    path("segnalazioni/<int:id>/delete", remove_segnalazioni),
    path("segnalazioni/update/<int:id>", update_segnalazioni),

    path("soluzioni/create", create_soluzioni),
    path("soluzioni/retrive_soluzioni", retrive_user_soluzioni),
    path("soluzioni/update/<int:id>", update_soluzioni),
    path("soluzioni/<int:id>/delete", remove_soluzioni),

    path("occorrenze/create", create_occorrenze),
    path("occorrenze/retrive_occorrenze", retrive_user_occurrenze),
    path("occorrenze/update/<int:id>", update_occurrenze),
    path("occorrenze/<int:id>/delete", remove_occorrenze),

    path("stati_soluzioni/create", create_stati_soluzione),
    path("stati_soluzioni/update/<int:id>", update_stati_soluzione),
    path("stati_soluzioni/<int:id>/delete", remove_stati_soluzione),
    
    path("stati_segnalazione/create", create_stati_segnalazione),
    path("stati_segnalazione/update/<int:id>", update_stati_segnalazione),
    path("stati_segnalazione/<int:id>/delete", remove_stati_segnalazione),

    path("admin/segnalazioni/retrive_segnalazioni", retrive_all_segnalazioni),
    path("admin/soluzioni/retrive_soluzioni", retrive_all_soluzioni),
    path("admin/occorrenze/retrive_occorrenze", retrive_all_occurrenze),
    path("admin/stati_soluzioni/retrive_stati_soluzioni", retrieve_all_stati_soluzioni),
    path("admin/stati_segnalazione/retrieve_stati_segnalazione", retrieve_all_stati_segnalazione),
]
