from django.db import models
from phone_field import PhoneField

class Patient(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=False)
    email = models.EmailField(max_length=100, blank=True)
    phone = PhoneField(blank=False, help_text='Contact phone number')
    county = models.CharField(max_length=30, blank=False)
    id_number = models.CharField(max_length=15, blank=False, unique=True)

    def __str__(self):
        name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        return name

class Appointment(models.Model):
    title = models.CharField(max_length=30, blank=False)
    attendant = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=500, blank=True)
    date_time = models.DateTimeField(blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
