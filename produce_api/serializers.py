from rest_framework import serializers
from .models import Produce

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        field = ('id', 'name', 'price', 'type',)