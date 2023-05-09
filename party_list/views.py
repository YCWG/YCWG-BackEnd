from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import Party

class PartyListAPIView(APIView):
    def get(self, request):
        queryset = Party.objects.all()
        serializer = PartySerializer(queryset, many=True)

        return Response(serializer.data)