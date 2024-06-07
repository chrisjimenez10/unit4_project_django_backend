from django.db import models

# Create your models here.
class Snacks(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)