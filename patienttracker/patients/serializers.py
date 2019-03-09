from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Patient
        fields = ('id', 'first_name', 'middle_name', 'last_name',
         'date_of_birth', 'date_created', 'date_modified',
         'gender', 'email', 'phone',
         'county', 'id_number')
        read_only_fields = ('date_created', 'date_modified')
