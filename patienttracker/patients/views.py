from rest_framework.viewsets import ModelViewSet
from .serializers import PatientSerializer, AppointmentSerializer
from .models import Patient, Appointment
from rest_framework_extensions.mixins import NestedViewSetMixin

class PatientViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
