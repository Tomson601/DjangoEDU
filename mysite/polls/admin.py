from django.contrib import admin

from .models import Car, Question, User

admin.site.register(Question)
# Register your models here.

admin.site.register(User)                       # Registering user model to admin GUI 
admin.site.register(Car)
