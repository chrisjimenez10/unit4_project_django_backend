from django.shortcuts import render
from rest_framework import generics
from .serializer import BeverageSerializer
from .models import Beverage

# Create your views here.
class BeveragesList(generics.ListCreateAPIView):
    queryset = Beverage.objects.all().order_by('id')
    serializer_class = BeverageSerializer

class BeverageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beverage.objects.all().order_by('id')
    serializer_class = BeverageSerializer
