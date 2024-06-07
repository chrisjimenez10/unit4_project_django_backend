from django.db import models
from django.utils import timezone

# Create your models here.
class Meat(models.Model):
    name = models.CharField(max_length=32)
    #Here, "type" refers to Meat (for search feature --> Implement later maybe...)
    type = models.CharField(max_length=32)
    description = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    packaged = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return F"{self.name}, {self.type}, {self.description}, {self.origin}, {self.packaged}, {self.price}"
