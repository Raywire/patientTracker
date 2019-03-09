from rest_framework import generics
from .serializers import PatientSerializer
from .models import Patient


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create_record(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()