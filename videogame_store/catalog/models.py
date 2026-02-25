from django.db import models

# Create your models here.
class Videogame(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    platform = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default='default.png')
    
    def __str__(self):
        return self.name


