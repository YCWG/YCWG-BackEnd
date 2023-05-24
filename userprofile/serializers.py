from rest_framework import serializers
from account import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'email', 'username', 'password', 'background_image', 'user_profile', 'user_bio')
        extra_kwargs = {'password': {'write_only' : True }}
    
    def create(self, validated_data):
        
        user = models.Account(
            email = validated_data['email'],
            name = validated_data['name'],
            is_admin = validated_data['is_admin'],
            background_image = validated_data['background_image'],
            user_profile = validated_data['user_profile'],
            user_bio = validated_data['user_bio']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user