from rest_framework import serializers
from .models import Snacks

class SnacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snacks
        fields = ('id', 'name', 'description', 'type', 'price',)