from rest_framework import serializers
from .models import Beverage

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ('id', 'name', 'description', 'type', 'price')