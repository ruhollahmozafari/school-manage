
import json
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# from apps.submissions.models import StudentSubmission
# from apps.projects.models import Project
from .models import UserProfile
# from .permissions import ObjectPermission
from .serializers import *
from .permissions import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()