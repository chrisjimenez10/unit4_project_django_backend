from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProduceSerializer
from .models import Produce

class ProduceList(generics.ListCreateAPIView):
    queryset = Produce.objects.all().order_by('id')
    serializer_class = ProduceSerializer

class ProduceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produce.objects.all().order_by('id')
    serializer_class = ProduceSerializer