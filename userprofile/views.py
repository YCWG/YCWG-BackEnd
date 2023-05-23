from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserProfileSerializer
from account import models


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.Account.objects.all()

