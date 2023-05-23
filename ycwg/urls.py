from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('partylist/', include("party_list.urls")),
    path('admin/', admin.site.urls),
    path('api/auth/', include('account.urls')),
    path('profile/', include('userprofile.urls')),
]