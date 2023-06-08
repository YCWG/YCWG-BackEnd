from rest_framework import serializers
from .models import *

class PartyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('title', 'category', 'place', 'member_limit', 'now_member', 'date', 'description', 'latitude', 'longitude',)

class PartyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('image',)