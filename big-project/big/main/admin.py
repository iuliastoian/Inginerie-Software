from django.contrib import admin
from .models import Patient, Appointment, MedicalReport, Receipt

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalReport)
admin.site.register(Receipt)