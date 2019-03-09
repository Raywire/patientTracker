import uuid
from django.db import models

class Patient(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    publicId = str(uuid.uuid4())
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    dateOfBirth = models.DateField(blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=False)
    email = models.CharField(max_length=60, blank=True)
    phone = models.IntegerField(blank=False)
    county = models.CharField(max_length=30, blank=False)
    nhif = models.CharField(max_length=15, blank=True)