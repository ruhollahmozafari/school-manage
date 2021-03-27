from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'studentcertificate',StudentCertificateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]