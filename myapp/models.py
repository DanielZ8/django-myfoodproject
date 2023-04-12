from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='food', blank=True)
    type = models.CharField(max_length = 20)
    kcal = models.IntegerField(default = 1)
    category = models.CharField(max_length = 30)
    recipe = models.CharField(max_length=300)
    

    