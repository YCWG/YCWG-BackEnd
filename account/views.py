from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from rest_framework import exceptions as rest_exceptiojns, response, decorators as rest_decoratros, permission as rest_permission
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serailizers, exceptions as rest_exceptions
from account import serializers, models

def get_user_token(user):
    refresh = tokens.RefreshToken.for_user(user)
    return(
        "refresh_token" : str(refresh),
        "access_token" : str(refresh.access_token)
    )

@rest_decoratros.api_view("POST")
@rest_decoratros.permission_classes([])
def loginView(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception = True)

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]

    user = authenticate(email=email, password=password)

    if user is not None:
        tokens = get_user_token(user)
        res = response.Response()
        res.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'],
            value = tokens["access_token"],
            expires= settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure= settings.SIMPLE_JWTp['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']

        )

        res.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            value = tokens["refresh_token"],
            expires= settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure= settings.SIMPLE_JWTp['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']

        )

        res.data = tokens
        res["X-CSRFToken"] = csrf.get_token(request)
        return res
    raise rest_exceptions.AuthenticationFailed(
        "Email or Password is incorrect")