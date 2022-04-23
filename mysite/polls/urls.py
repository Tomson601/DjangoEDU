from email.mime import base
from posixpath import basename
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views                                                             # "." means current directory


router = routers.DefaultRouter()
router.register("coffee", views.CoffeeViewSet, basename="coffee")
router.register("car", views.CarViewSet, basename="car")
router.register("clock", views.ClockViewSet, basename="clock")
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path('', views.index, name='index'),
    path('getting/', views.getting, name='getting'),
    url(r"^", include(router.urls)),
]
