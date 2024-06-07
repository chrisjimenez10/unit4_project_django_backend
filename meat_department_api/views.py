from django.shortcuts import render
from rest_framework import generics
from .serializers import MeatSerializer
from .models import Meat

# Create your views here.
class MeatList(generics.ListCreateAPIView):
    queryset = Meat.objects.all().order_by('id')
    serializer_class = MeatSerializer

class MeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meat.objects.all().order_by('id')
    serializer_class = MeatSerializer