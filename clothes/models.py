from django.db import models

class Category(models.Model):
    name  = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to='clothingimages')


    def __str__(self):
        return self.name


# Create your models here.
