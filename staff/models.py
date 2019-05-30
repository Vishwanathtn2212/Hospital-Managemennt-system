from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from hospital.models import Person


# Create your models here.
class Doctor(Person):

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
