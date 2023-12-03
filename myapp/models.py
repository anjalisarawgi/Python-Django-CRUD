from django.db import models

# Create your models here.


class User(models.Model):
    is_gender={
        ('male', 'Male'),
        ('female', 'Female')
    }

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    gender= models.CharField(choices=is_gender, max_length=100)


def __str__(self):
    return self.name