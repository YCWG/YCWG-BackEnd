from django.urls import path
from .views import PartyListAPIView, PartyListDetailAPIView, PartyImageAPIView

urlpatterns = [
    path('', PartyListAPIView.as_view(), name = "partylist"),
    path("<int:pk>/", PartyListDetailAPIView.as_view(), name = "partylist_detail"),
    path("image/", PartyImageAPIView.as_view(), name = "partyimage")
]