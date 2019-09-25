from django.db import models

from django.utils import timezone
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length=200)
    publishDate = models.DateField()