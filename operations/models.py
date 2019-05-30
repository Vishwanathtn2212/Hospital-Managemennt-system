from django.db import models

# Create your models here.
from django.utils import timezone

from core.models import TimeStampedModel
from reception.models import Patient
from hospital.models import Diagnose
from staff.models import Doctor


# Create your models here.


class Treatment(models.Model):
    date = models.DateField(default=timezone.now().date())
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=None)
    symptoms = models.TextField()
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctors_comments = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.patient, self.diagnosis)
