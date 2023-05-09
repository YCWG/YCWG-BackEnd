from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView


from .serializers import *
from .models import Party

class PartyListAPIView(ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)