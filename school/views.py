
import json
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .models import UserProfile
from .serializers import *
from .permissions import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class StudentCertificateViewSet(viewsets.ModelViewSet):
    queryset = StudentsCertificate.objects.all()
    serializer_class = StudentCertificateSerializer










