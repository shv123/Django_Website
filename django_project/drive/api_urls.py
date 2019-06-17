from django.urls import path
from . import views
from rest_framework import routers
from drive.views import *
from django.urls import include

#router = routers.DefaultRouter()
#router.register('', DriveViewSet)

#urlpatterns = [
#    path('drive/', include(router.urls)),
#]