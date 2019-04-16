from django.db import models

# Create your models here.
class Flat(models.Model):
    city_name = models.CharField(max_length=50, unique=True)
    flat_flor= models.TextField()

    def __str__(self):
        return self.city_name

class Shop(models.Model):
    city_name = models . CharField(max_length=50, unique=True)
    shop_flor = models . TextField()

    def __str__(self):
        return self.city_name

