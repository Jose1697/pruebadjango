from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.CharField(max_length=300)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=200)







