from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

#Register/Validate User serializer
class RegisterSerializer(serializers.ModelSerializer):
    #Here, we are creating a serializer field for both password and confirm password - 'write_only=True' means that this field is only used for writing data and WILL NOT be included in serialized representations (In other words, the password will NOT be displayed in JSON format and kept hidden) --> The 'validators=[validate_password]' parameter is using Django's built-in password validation to ensure password meets criteria like lenght, complexity, etc.
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmpassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirmpassword', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
        }

    #Here, we are creating a validation function for further validation to our serialized fields
    def validate(self, attrs):
        #Validation and error handling to ensure "password" matches "confirm password"
            #The syntax attrs["password"] is dictionary syntax to acces the individual field
        if attrs['password'] != attrs['confirmpassword']:
            #Here, the keyword "raise" means that it raises a "serializers.ValidationError", which means that we can send a custom error message in JSON format 
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        #Validation and error handling to ensure that our "first_name" field is NOT empty --> With the additional argument to our field in lines 23-25, when I created a user with an empy string it was created regardless of field being an empty string, so with this validation I ensured that user will not be created unless something is typed in for "first_name"
        if attrs['first_name'] == "":
            raise serializers.ValidationError({"first_name": "Name field empty, please provide your first name"})

        return attrs

    #This create() function uses the create() method to create a new User instance with the validated data 
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        #Here, "user.set_password()" is setting the newly created User object's password to the password provided and after it is validated, which is why we use the "confirmpassword" field --> Also, this method HASHES (encrypts) the password BEFORE storing it to the database
        user.set_password(validated_data['confirmpassword'])
        #Here, we are SAVING the newly created User object to the database
        user.save()

        return user

#Serializer for listing users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')