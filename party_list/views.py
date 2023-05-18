from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import Party

class PartyListAPIView(APIView):
    def get(self, request):
        queryset = Party.objects.all()
        serializer = PartyListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PartyListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)