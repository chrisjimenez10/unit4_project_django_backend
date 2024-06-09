from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MeatSerializer
from .models import Meat

# Create your views here.
class MeatList(generics.ListCreateAPIView):
    queryset = Meat.objects.all().order_by('id')
    serializer_class = MeatSerializer

    permission_classes = [IsAuthenticated]

class MeatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meat.objects.all().order_by('id')
    serializer_class = MeatSerializer

    #Setting a "permission_classes" attribute to our Classes to ENSURE that these views (Referring to ".RetrieveUpdateDestroyAPIView" and ".ListCreateAPIView") are protected and can only be viewed by an authenticated user
    permission_classes = [IsAuthenticated]
