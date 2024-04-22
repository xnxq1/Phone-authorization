from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import apiViewSet

router = DefaultRouter()
router.register(r'users', apiViewSet, basename='user')
urlpatterns = router.urls
app_name = 'API'

