from django.db import models

# Create your models here.
from django.template.defaultfilters import truncatechars
from django.utils import timezone

# project imports
from core.models import TimeStampedModel
from hospital.models import Person, Room, Diagnose
from staff.models import Doctor


class Patient(Person):

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class In_patient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_adm = models.DateField(default=timezone.now().date())
    date_of_discarge = models.DateField()
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctor = models.ForeignKey(Doctor, on_delete=None)
    room = models.ForeignKey(Room, on_delete=None)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.room)


class Out_patient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now().date())
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctor = models.ForeignKey(Doctor, on_delete=None)

    def __str__(self):
        return '{}'.format(self.patient)
