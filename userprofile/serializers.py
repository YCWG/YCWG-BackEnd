from rest_framework import serializers
from account import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only' : True }}
    
    def create(self, validated_data):
        
        user = models.Account(
            email = validated_data['email'],
            name = validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user