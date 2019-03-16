from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet, AppointmentViewSet
from django.urls import path, include

router = DefaultRouter()
 
router.register('api/v1/patients', PatientViewSet)
router.register('api/v1/appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
