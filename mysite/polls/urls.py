from posixpath import basename
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views                                                             # "." means current directory


router = routers.DefaultRouter()
router.register("coffee", views.CoffeeViewSet, basename="coffee")
router.register("car", views.CarViewSet, basename="car")

urlpatterns = [
    path('', views.index, name='index'),
    path('getting/', views.getting, name='getting'),    # 1-Nazwa url, 2- views.X 3- nazwa
    url(r"^", include(router.urls)),
]
