from django.db import models
from accounts.models import Doctor, Nurse

# tabel in baza de date pentru inregistrarea unui pacient,
# care are atribuite campurile mentionate
class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10)

# tabel in baza de date pentru inregistrarea unei programari,
# care are atribuite campurile mentionate
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, unique=False)            # cheie straina doctor
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, unique=False)          # cheie straina pacient
    time = models.CharField(max_length=40)
    date = models.CharField(max_length=40)

# tabel in baza de date pentru inregistrarea unei fise de diagnosticare,
# care are atribuite campurile mentionate
class MedicalReport(models.Model):
    date = models.DateField(auto_now=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, unique=False)            # cheie straina doctor
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, unique=False)          # cheie straina pacient
    symptoms = models.CharField(max_length=200)
    prescription = models.CharField(max_length=200)

# tabel in baza de date pentru inregistrarea unei chitante,
# care are atribuite campurile mentionate
class Receipt(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, unique=False)            # cheie straina doctor
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, unique=False)          # cheie straina pacient
    time = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    pay = models.IntegerField(default=0)
