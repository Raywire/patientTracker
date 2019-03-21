from users.views import UserViewSet
from django.urls import path, include
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
