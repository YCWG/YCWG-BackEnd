from django.urls import path, include

urlpatterns = [
    path('partylist/', include("party_list.urls"))
]