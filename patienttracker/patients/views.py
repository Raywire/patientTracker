from rest_framework import generics
from .serializers import PatientSerializer
from .models import Patient


class CreateView(generics.ListCreateAPIView):
    """This class defines the method to create a patient record."""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @classmethod
    def create_record(cls, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
