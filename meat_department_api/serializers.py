from rest_framework import serializers
#Imports to validate and create user
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Meat

# Meat Serializer
class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meat
        fields = ('id', 'name', 'type', 'description', 'origin', 'price')

#Register/Validate User serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirmpassword', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmpassword']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['confirmpassword'])
        user.save()

        return user

#Serializer for listing users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
