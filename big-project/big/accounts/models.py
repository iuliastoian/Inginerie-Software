from django.db import models
from django.contrib.auth.models import User

# tabel in baza de date pentru inregistrarea unui doctor,
# care are atribuite campurile mentionate
class Doctor(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.OneToOneField(User, on_delete = models.CASCADE)    # legatura unu-la-unu cu User
    email = models.CharField(max_length=50, unique=True)
    is_doctor = models.BooleanField(default=True)
    is_nurse = models.BooleanField(default=False)


# tabel in baza de date pentru inregistrarea unei asistente,
# care are atribuite campurile mentionate
class Nurse(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.OneToOneField(User, on_delete = models.CASCADE)    # legatura unu-la-unu cu User
    email = models.CharField(max_length=50, unique=True)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=True)
   