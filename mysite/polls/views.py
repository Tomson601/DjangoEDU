#from django.shortcuts import render
from django.http import HttpResponse
from polls import serializers, models
from rest_framework.viewsets import ModelViewSet

# Creating ViewSet for model

def index(request):
    return HttpResponse("Hello, world") # Returning "Hello, world" on the site

def getting(request):
    return  HttpResponse("getting polls...")

class CoffeeViewSet(ModelViewSet):
    queryset = models.Coffee.objects.all()
    serializer_class = serializers.CoffeeSerializer

class CarViewSet(ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    
class ClockViewSet(ModelViewSet):
    queryset = models.Clock.objects.all()
    serializer_class = serializers.ClockSerializer

class UserViewSet(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class DogViewSet(ModelViewSet):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer
