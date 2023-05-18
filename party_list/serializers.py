from rest_framework import serializers
from .models import *

class PartyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'