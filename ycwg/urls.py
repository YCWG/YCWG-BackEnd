from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('partylist/', include("party_list.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls'))
]