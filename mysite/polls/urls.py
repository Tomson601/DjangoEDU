from email.mime import base
from posixpath import basename
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views                                                             # "." means current directory


router = routers.DefaultRouter()
router.register("coffee", views.CoffeeViewSet, basename="coffee")
router.register("cars", views.CarViewSet, basename="cars")
router.register("clock", views.ClockViewSet, basename="clock")
router.register("users", views.UserViewSet, basename="users")
router.register("dog", views.DogViewSet, basename="dog")

urlpatterns = [
    path('', views.index, name='index'),
    path('getting/', views.getting, name='getting'),
    url(r"^", include(router.urls)),
]
