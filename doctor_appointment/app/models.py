from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()
    specialty = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    available_days = models.CharField(max_length=100)  
    available_time_start = models.TimeField()
    available_time_end = models.TimeField()



class Patient(models.Model):
    Patient_name = models.CharField(max_length=100)
    age  = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)
