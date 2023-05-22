from django.urls import path
from .views import PartyListAPIView, PartyListDetailAPIView

urlpatterns = [
    path('', PartyListAPIView.as_view(), name = "partylist"),
    path("<int:pk>/", PartyListDetailAPIView.as_view(), name = "partylist_detail")
]