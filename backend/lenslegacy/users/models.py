from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    firstname= models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__ (self):
        return self.user_name; 
    