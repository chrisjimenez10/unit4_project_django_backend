from rest_framework import serializers
from .models import Meat

#Serializer
class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = ('id', 'name', 'type', 'description', 'origin', 'packaged', 'price')