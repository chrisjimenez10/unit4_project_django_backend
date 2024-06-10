from rest_framework import serializers
#Imports to validate and create user

from .models import Meat

# Meat Serializer
class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = ('id', 'name', 'type', 'description', 'origin', 'price')
