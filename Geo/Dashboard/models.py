from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def _str_(self):
        return self.name 

class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.customer.username}-Profile'
class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.name 
class Volunteers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.name 

class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    volunteers = models.ManyToManyField(Volunteers)
    def _str_(self):
        return self.name 
# Create your models here.
