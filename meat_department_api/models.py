from django.db import models
from django.utils import timezone

# Create your models here.
class Meat(models.Model):
    name = models.CharField(max_length=32)
    #Here, for "type" field we want it to be "Meat" with every entry item --> We can do that by setting a default value and "editable" parameter set to False, so that users CANNOT change the value - With this, every new entry will have the default value of "Meat" and we don't have to worry about a user editing the field
    type = models.CharField(max_length=32, default='Meat', editable=False)
    description = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    packaged = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return F"{self.name}, {self.type}, {self.description}, {self.origin}, {self.packaged}, {self.price}"
