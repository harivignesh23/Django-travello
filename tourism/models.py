from django.db import models

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    desc =models.CharField(max_length=200)
    image =models.ImageField(upload_to="pics")
    price : models.IntegerField()


class popular(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics1")
    price : models.IntegerField()

     




   