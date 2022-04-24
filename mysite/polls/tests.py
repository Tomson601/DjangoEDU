from mimetypes import init
from urllib import response
from .models import Car, Dog, User, Clock
from django.test import Client
import pytest

@pytest.mark.django_db                                                                          # Adding access to database
class TestUser:                                                                                 # Initiation of Test class
    def test_api_connection(self):
        c = Client()                                                                            # "Fake postman"

        User.objects.create(name = "Mariusz", age = "69", account_type = "User")
        User.objects.create(name = "Bożydar", age = "18")

        response = c.get("/polls/users/")

        assert response.status_code == 200                                                      # Checking if status code equals to 200
        assert response.json() == [{'account_type': 'User', 'age': '69', 'cars':[], 'id': 1, 'name': 'Mariusz'}, {'account_type': 'User', 'age': '18', 'cars':[], 'id': 2, 'name': 'Bożydar'}]

    def test_cars(self):
        c = Client()

        user = User.objects.create(name = "Mariusz", age = "69", account_type = "User")
        car = Car.objects.create(brand = "MegaCar", model="xd", price = "21", user = user)

        response = c.get("/polls/cars/")

        assert response.status_code == 200
        assert response.json() == [{'brand': 'MegaCar',  'id': 1,  'is_broken': False,  'model': 'xd',  'price': 21.0,  'user': 1}]
    
    def test_dog(self):
        c = Client()

        dpg = Dog.objects.create(name = "Piesel")

        response = c.get("/polls/dog/")

        assert response.status_code == 200
        assert response.json() == [{'id': 1, 'name': 'Piesel'}]
