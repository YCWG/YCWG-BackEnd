from rest_framework import serializers
from .models import *

class PartyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class PartyImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Image
        fields = ['image', 'image_url']

    def get_image_url(self, obj):
        return obj.image.url
