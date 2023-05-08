from django.db import models
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Volunteers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    volunteers = models.ManyToManyField(Volunteers)
# Create your models here.
