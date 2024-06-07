from django.shortcuts import render
from rest_framework import generics
from .serializers import SnacksSerializer
from .models import Snacks

# Create your views here.
class SnacksList(generics.ListCreateAPIView):
    queryset = Snacks.objects.all().order_by('id')
    serializer_class = SnacksSerializer

class SnacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snacks.objects.all().order_by('id')
    serializer_class = SnacksSerializer