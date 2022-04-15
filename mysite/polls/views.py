#from django.shortcuts import render
from django.http import HttpResponse
from polls import serializers, models
from rest_framework.viewsets import ModelViewSet

# Create your views here.
# Tworzymy widok, który trzeba zmapowować z URL'em

def index(request):                     # Zdefiniowanie requestu
    return HttpResponse("Hello, world") # Zwrócenie "Hello, world"

def getting(request):
    return  HttpResponse("getting polls...")

class CoffeeViewSet(ModelViewSet):
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class CarViewSet(ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    