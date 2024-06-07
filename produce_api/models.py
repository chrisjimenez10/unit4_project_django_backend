from django.db import models

# Create your models here.
class Produce(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=20)