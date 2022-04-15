from operator import mod
from pickle import FALSE
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):                                               # Define new model
    question_text = models.CharField(max_length=150)                        # Name of instance --> question_text it's char type and can take up to 200 chars
    pub_date = models.DateTimeField('date published')
    def __str__(self):                                                      # Define how to print data 
        return self.pub_date.strftime("%Y-%m-%dT%H:%M")                     #
    def was_published_recently(self):                                       # Creating was_published_recently method
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text

class Coffee(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    tasty = models.BooleanField(default=True)

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.FloatField(max_length=100)
    is_broken = models.BooleanField(default=False)