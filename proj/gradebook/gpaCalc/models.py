from django.db import models

# Create your models here.

class Class(models.Model):
    userID = models.CharField(max_length = 200)
    name = models.CharField(max_length=200)
    letterGrade = models.CharField(max_length = 1)
