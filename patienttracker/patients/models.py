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
    nhif = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
