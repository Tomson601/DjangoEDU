from dataclasses import fields
from rest_framework import serializers
from polls import models                                                            # Importing models from polls 

class CoffeeSerializer(serializers.HyperlinkedModelSerializer):                      # Creating serializer for Coffee
    class Meta:
        model = models.Coffee
        fields = ('id', 'name', 'price', 'size', 'brand', 'tasty')                        # Fields that will be visable from API view

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Car
        fields = ('id', 'brand', 'model', 'price', 'is_broken')

class ClockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Clock
        fields = ('id', 'brand', 'time', 'price')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'name', 'age')
