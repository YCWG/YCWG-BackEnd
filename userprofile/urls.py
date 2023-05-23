from django.urls import path, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]