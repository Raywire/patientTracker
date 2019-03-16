from rest_framework.viewsets import ModelViewSet
from .serializers import PatientSerializer, AppointmentSerializer
from .models import Patient, Appointment

class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
