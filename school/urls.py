from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]