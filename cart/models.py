from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='cartimages')
    price = models.FloatField()
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.name
# Create your models here.
