from django.urls import path
from account.views import *

app_name = "accout"

urlpatterns = [
    path('csrf/', get_csrf.as_view(), name = 'api-csrf'),
    path('login/', loginView.as_view(), name = "api-login")
]