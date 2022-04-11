from django.urls import path
from . import views             # Z "."- (obecnego katalogu) importujemy views (plik pythonowy)


urlpatterns = [
    path('', views.index, name='index'),
    path('getting/', views.getting, name='getting'),    # 1-Nazwa url, 2- views.X 3- nazwa
]
