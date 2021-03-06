from patients.views import PatientViewSet, AppointmentViewSet
from django.urls import path, include
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()

patients_router = router.register('api/v1/patients', PatientViewSet)
appointment_router = router.register('api/v1/appointments', AppointmentViewSet)
patients_router.register(
    'appointments', AppointmentViewSet,
    base_name='patient-appointments',
    parents_query_lookups=['patient'])

urlpatterns = [
    path('', include(router.urls))
]
