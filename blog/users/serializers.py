from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#Creating serializer which will convert users data to json 
#password of length 8
#Model of serializer is default user class hence defined in Meta
#write_true means password field will only visible when post request, not in get request

class UserSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data) 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user): #override get_token method
        token = super().get_token(user) #call super class get token method
        token['username'] = user.username #add current username in token
        token['email'] = user.email # add email in token
        return token