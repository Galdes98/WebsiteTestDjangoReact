#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def main(request):
#    return HttpResponse("Hello")

from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()  
    serializer_class = RoomSerializer  
