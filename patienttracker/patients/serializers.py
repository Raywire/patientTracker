from rest_framework import serializers
from .models import Patient, Appointment

class PatientSerializer(serializers.ModelSerializer):
    """Serializer to map the Patient Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Patient
        fields = ('id', 'first_name', 'middle_name', 'last_name',
         'date_of_birth', 'date_created', 'date_modified',
         'gender', 'email', 'phone',
         'county', 'id_number')
        read_only_fields = ('date_created', 'date_modified')

class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer to map the Appointment Model instance into JSON format."""
    class Meta:
        """Maps the appointment serializer's fields with its model fields"""
        model = Appointment
        fields = ('id', 'title', 'attendant', 'description',
         'date_created', 'date_modified',
         'date_time', 'patient')
        read_only_fields = ('date_created', 'date_modified')
