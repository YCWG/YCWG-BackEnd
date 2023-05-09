from django.urls import path
from .views import PartyListAPIView

urlpatterns = [
    path('',PartyListAPIView.as_view(), name = "partyList" ),
]