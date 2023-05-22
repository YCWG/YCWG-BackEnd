from rest_framework import serializers
from django.conf import settings
from account.models import Account

class RegisterationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style = {"input_type" : "password"})

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            "password": {"write_only" : True},
            "password2": {"write_only": True}
        }

    def save(self):
        user = settings.AUTH_USER_MODEL(
            email = self.validated_data["email"],
            username = self.validated_data["username"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"passwrod" : "Passwords do not match!"})
        
        user.set_password(password)
        user.save()

        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(stype = {"input_type" : "password"}, write_only = True)

