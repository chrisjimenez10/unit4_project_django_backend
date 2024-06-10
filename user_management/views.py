from django.shortcuts import render
from rest_framework import generics
#Import "IsAuthenticated" for Login feature - validate user credentials
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
#Import "RegisterSerializer" to create view for user creation and "AllowAny" to allow permission for all to access view and regiter a user account and User model
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer

#Create User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    #The "permission_classes" attribute specifies which permissions are required to access a particular view. It allows us to control who can access our API endpoints based on various criteria
        #The "AllowAny" permission class is one of the built-in permission classes provided by DRF and it means that the view is accessible to any user, regardless of whether they are authenticated or not
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#Display List of Users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

#Update, Delete, View single User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer