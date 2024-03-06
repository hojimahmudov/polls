from django.db.models import Model
from django.db import models


# Create your models here.

class Question(Model):
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Option(Model):
    text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
