from django.db import models



class Jewelry(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='jewelimages')


    def __str__(self):
        return self.name
# Create your models here.
