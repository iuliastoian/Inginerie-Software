from django.shortcuts import render, redirect
from accounts.models import Doctor, Nurse
from main.models import Patient, Appointment, MedicalReport, Receipt
from django.core.mail import send_mail
from big.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from django.template.loader import get_template
from .utils import render_to_pdf

# pentru actiunea de a naviga spre pagina principala home
def home(response):
    return render(response, "main/home.html", {}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina cu meniul functionalitatilor unui doctor
def doctor_menu(response):
    return render(response, "main/doctor_menu.html", {}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina cu meniul functionalitatilor unui asistent
def nurse_menu(response):
    return render(response, "main/nurse_menu.html", {}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de adaugare a unui pacient
def add_patient(response):
    if response.method == "POST":
        # se inregistreaza un nou pacient in baza de date, cu datele introduse de catre utilizator
        new_patient = Patient(full_name=response.POST.get('full_name'), email=response.POST.get('email'), gender=response.POST.get('gender'))
        new_patient.save()

        return redirect('/nurse_menu') # se redirectioneaza spre pagina meniu pt asistenti

    return render(response, "main/add_patient.html", {}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de programare consultatie
def schedule_appointment(response):
    patient_names = Patient.objects.all()  # se stocheaza toate obiectele de tip pacient
    doctor_names = Doctor.objects.all()    # se stocheaza toate obiectele de tip doctor

    if response.method == "POST":
        doctor_id = int(response.POST.get('doctor'))        # id-ul doctorului ales
        patient_id = int(response.POST.get('patient'))      # id-ul pacientului ales

        doctor_input = Doctor.objects.get(pk=doctor_id)     # returneaza obiectul de tip doctor cu id-ul respectiv
        patient_input = Patient.objects.get(pk=patient_id)  # returneaza obiectul de tip pacient cu id-ul respectiv

        # se inregistreaza o noua programare in baza de date, cu datele introduse de catre utilizator
        new_appointment = Appointment(doctor=doctor_input, patient=patient_input, time=response.POST.get('time'), date=response.POST.get('date'))
        new_appointment.save()

        return redirect('/nurse_menu') # se redirectioneaza spre pagina meniu pt asistenti
    
    # se transmit prin dictionar obiectele de tip pacient si doctor
    return render(response, "main/schedule_appointment.html", {'patient_names':patient_names, 'doctor_names':doctor_names}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de creare fisa medicala
def create_medical_report(response):
    patient_names = Patient.objects.all()  # se stocheaza toate obiectele de tip pacient
    doctor_names = Doctor.objects.all()    # se stocheaza toate obiectele de tip doctor

    if response.method == "POST":
        doctor_id = int(response.POST.get('doctor'))        # id-ul doctorului ales
        patient_id = int(response.POST.get('patient'))      # id-ul pacientului ales

        doctor_input = Doctor.objects.get(pk=doctor_id)     # returneaza obiectul de tip doctor cu id-ul respectiv
        patient_input = Patient.objects.get(pk=patient_id)  # returneaza obiectul de tip pacient cu id-ul respectiv

        # se inregistreaza o noua fisa medicala in baza de date, cu datele introduse de catre utilizator
        new_medical_report = MedicalReport(doctor=doctor_input, patient=patient_input, date=response.POST.get('date'), symptoms=response.POST.get('symptoms'), prescription=response.POST.get('prescription'))
        new_medical_report.save()

        return redirect('/doctor_menu') # se redirectioneaza spre pagina meniu pt doctori

    # se transmit prin dictionar obiectele de tip pacient si doctor
    return render(response, "main/create_medical_report.html", {'patient_names':patient_names, 'doctor_names':doctor_names}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de creare chitanta
def create_receipt(response):
    patient_names = Patient.objects.all()   # se stocheaza toate obiectele de tip pacient
    doctor_names = Doctor.objects.all()     # se stocheaza toate obiectele de tip doctor

    if response.method == "POST":
        doctor_id = int(response.POST.get('doctor'))         # id-ul doctorului ales
        patient_id = int(response.POST.get('patient'))       # id-ul pacientului ales

        doctor_input = Doctor.objects.get(pk=doctor_id)     # returneaza obiectul de tip doctor cu id-ul respectiv
        patient_input = Patient.objects.get(pk=patient_id)  # returneaza obiectul de tip pacient cu id-ul respectiv

        # se inregistreaza o noua chitanta in baza de date, cu datele introduse de catre utilizator
        new_receipt = Receipt(doctor=doctor_input, patient=patient_input, time=response.POST.get('time'), date=response.POST.get('date'), pay=response.POST.get('pay'))
        new_receipt.save()

        return redirect('/nurse_menu') # se redirectioneaza spre pagina meniu pt asistenti
    
    # se transmit prin dictionar obiectele de tip pacient si doctor
    return render(response, "main/create_receipt.html", {'patient_names':patient_names, 'doctor_names':doctor_names}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de trimitere reminder
def set_reminder(response):
    patients = Patient.objects.all()             # se stocheaza toate obiectele de tip pacient
    appointments = Appointment.objects.all()     # se stocheaza toate obiectele de tip programare

    if response.method == "POST":
        patient_id = int(response.POST.get('patient'))      # id-ul pacientului ales
        patient_input = Patient.objects.get(pk=patient_id)  # returneaza obiectul de tip pacient cu id-ul respectiv
        email = patient_input.email                         # se extrage din campurile pacientului ales si se stocheaza adresa lui de email
        
        subject = "Appointment Reminder"                            # subiectul mail-ului
        message = "Don't forget about your doctor's appointment!"   # mesajul mail-ului
        recepient = [email]                                         # destinatar

        send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)  # trimite mail pacientului

        return redirect('/nurse_menu') # se redirectioneaza spre pagina meniu pt asistenti

    # se transmit prin dictionar obiectele de tip pacient si programare
    return render(response, "main/set_reminder.html", {'patients':patients, 'appointments':appointments}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare pacienti a asistentilor
def view_patients(response):
    patients = Patient.objects.all()            # se stocheaza toate obiectele de tip pacient

    # se transmit prin dictionar obiectele de tip pacient
    return render(response, "main/view_patients.html", {'patients':patients}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare programari a asistentilor
def view_appointments(response):
    appointments = Appointment.objects.all()    # se stocheaza toate obiectele de tip programare

    # se transmit prin dictionar obiectele de tip programare
    return render(response, "main/view_appointments.html", {'appointments':appointments}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare pacienti a doctorilor
def view_patients0(response):
    patients = Patient.objects.all()            # se stocheaza toate obiectele de tip pacient

    # se transmit prin dictionar obiectele de tip pacient
    return render(response, "main/view_patients0.html", {'patients':patients}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare programari a doctorilor
def view_appointments0(response):
    appointments = Appointment.objects.all()    # se stocheaza toate obiectele de tip programare

    # se transmit prin dictionar obiectele de tip programare
    return render(response, "main/view_appointments0.html", {'appointments':appointments}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina cu meniul functionalitatilor unui vizitator
def guest(response):
    return render(response, "main/guest.html", {}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina care contine functionalitatea vizitatorului de vizualizare programari
def guest_appointments(response):
    appointments = Appointment.objects.all()    # se stocheaza toate obiectele de tip programare

    # se transmit prin dictionar obiectele de tip programare
    return render(response, "main/guest_appointments.html", {'appointments':appointments}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare fise medicale
def print_medical_report(response):
    medical_reports = MedicalReport.objects.all()    # se stocheaza toate obiectele de tip fisa medicala
    
    if response.method == "POST":
        medical_report_id = int(response.POST.get('all_medical_reports'))      # id-ul fisei medicale alese
        medical_report_input = MedicalReport.objects.get(pk=medical_report_id)     # returneaza obiectul de tip fisa medicala cu id-ul respectiv

        context = {"id": medical_report_id, "doctor": medical_report_input.doctor, "patient": medical_report_input.patient, "date": medical_report_input.date, "symptoms": medical_report_input.symptoms, "prescription": medical_report_input.prescription}
        pdf = render_to_pdf('pdf_output.html', context)

        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not Found")

    # se transmit prin dictionar obiectele de tip programare
    return render(response, "main/print_medical_report.html", {'medical_reports':medical_reports}) # se randeaza pagina web dupa template-ul descris

# pentru actiunea de a naviga spre pagina de vizualizare fise medicale
def print_receipt(response):
    receipts = Receipt.objects.all()    # se stocheaza toate obiectele de tip chitanta
    
    if response.method == "POST":
        receipt_id = int(response.POST.get('all_receipts'))      # id-ul chitantei alese                                                                
        receipt_input = Receipt.objects.get(pk=receipt_id)       # returneaza obiectul de tip chitanta cu id-ul respectiv

        context = {"id": receipt_id, "doctor": receipt_input.doctor, "patient": receipt_input.patient, "date": receipt_input.date, "time": receipt_input.time, "pay": receipt_input.pay}
        pdf = render_to_pdf('pdf_output_receipt.html', context)

        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not Found")

    # se transmit prin dictionar obiectele de tip programare
    return render(response, "main/print_receipt.html", {'receipts':receipts}) # se randeaza pagina web dupa template-ul descris
    
