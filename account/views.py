from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from rest_framework import exceptions as rest_exceptions, response, decorators as rest_decorators, permissions as rest_permissions
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions
from account import serializers, models


def get_user_token(user):
    refresh = tokens.RefreshToken.for_user(user)
    return{
        "access_token" : str(refresh.access_token),
        "refresh_token" : str(refresh)
    }

@rest_decorators.api_view("POST")
@rest_decorators.permission_classes([])
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

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([])
def registerView(request):
    serializer = serializers.RegisterationSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    if user is not None:
        return response.Response("Registered!")
    return rest_exceptions.AuthenticationFailed("Invalid credentials!")

@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticatied])
def logoutView(request):
    try:
        refreshToken = request.COOKIE.get(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        token = tokens.RefreshToken(refreshToken)
        token.blacklist()

        res = response.Response()
        res.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
        res.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        res.delete_cookie("X-CSRFToken")
        return res
    except:
        raise rest_exceptions.ParseError("Invalid token")

class CookieTokenRefreshSerializer():
    pass

class CookieTokenRefreshView(jwt_views.TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                value = response.data['refresh'],
                expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

            del response.data['refresh']
        response["X-CSRFToken"] = request.COOKIES.get("csrftoken")
        return super().finalize_response(request, response, *args, **kwargs)