from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    available_days = models.CharField(max_length=100)  
    available_time_start = models.TimeField()
    available_time_end = models.TimeField()