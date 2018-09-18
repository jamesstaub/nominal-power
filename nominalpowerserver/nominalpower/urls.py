from django.contrib import admin
from django.urls import path
from installations.views import installation
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/installations/', installation),
    # path('api/installations/', Installation.as_view()),
]
