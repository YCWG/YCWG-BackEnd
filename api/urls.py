from django.urls import path
from .views import PartyListAPIView

urlpatterns = [
    path('partylist/',PartyListAPIView.as_view(), name = "partyList" ),
]