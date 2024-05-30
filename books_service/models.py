from django.db import models
from enum import Enum
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='static/', null=True, blank=True)



class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True,blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='media/', null=True, blank=True)
    price_in = models.IntegerField(null=False, blank=False)
    price_out = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    bought = models.DateTimeField(null=True, blank=True)
    sold = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)