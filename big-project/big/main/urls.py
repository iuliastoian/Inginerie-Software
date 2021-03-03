from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),                                                           # pagina principala home
    path('doctor_menu/', views.doctor_menu, name="doctor_menu"),                                 # meniul pentru doctori
    path('nurse_menu/', views.nurse_menu, name="nurse_menu"),                                    # meniul pentru asistenti
    path('add_patient/', views.add_patient, name="add_patient"),                                 # pagina de adaugare pacient (tine de asistent)
    path('schedule_appointment/', views.schedule_appointment, name="schedule_appointment"),      # pagina de programare consultatie (tine de asistent)
    path('create_medical_report/', views.create_medical_report, name="create_medical_report"),   # pagina de creare fisa medicala (tine de doctor)
    path('set_reminder/', views.set_reminder, name="set_reminder"),                              # pagina de trimitere reminder (tine de asistent)
    path('create_receipt/', views.create_receipt, name="create_receipt"),                        # pagina de creare chitanta (tine de asistent)
    path('view_patients/', views.view_patients, name="view_patients"),                           # pagina de vizualizare pacienti (tine de aistent)
    path('view_appointments/', views.view_appointments, name="view_appointments"),               # pagina de vizualizare programari (tine de aistent)
    path('view_patients0/', views.view_patients0, name="view_patients0"),                        # pagina de vizualizare pacienti (tine de doctor)
    path('view_appointments0/', views.view_appointments0, name="view_appointments0"),            # pagina de vizualizare programari (tine de doctor)
    path('guest/', views.guest, name="guest"),                                                   # meniu pentru vizitatori
    path('guest_appointments', views.guest_appointments, name="guest_appointments"),             # pagina de vizualizare programari (tine de vizitator)
    path('print_medical_report/', views.print_medical_report, name="print_medical_report"),      # exportare format pdf
    path('print_receipt/', views.print_receipt, name="print_receipt"),                           # exportare format pdf
]