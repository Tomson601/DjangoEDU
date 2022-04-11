#from django.shortcuts import render
from django.http import HttpResponse    # Z modułu django.http zaimportuj klasę HttpResponse

# Create your views here.
# Tworzymy widok, który trzeba zmapowować z URL'em

def index(request):                     # Zdefiniowanie requestu
    return HttpResponse("Hello, world") # Zwrócenie "Hello, world"

def getting(request):
    return  HttpResponse("getting some polls...")