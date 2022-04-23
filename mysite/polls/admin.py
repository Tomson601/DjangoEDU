from django.contrib import admin

from .models import Question, User

admin.site.register(Question)
# Register your models here.

admin.site.register(User)
