from rest_framework.views import APIView 
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class UsersAPIView(APIView):
    #get used to display list of all users.
    #url for testing api = /myapi/users/
    def get(self, request):
        users = User.objects.all() #get all users for DB
        serializer = UserSerializer(users, many = True) #serialize the users data
        return Response(serializer.data) #return serialized users data as a response
    
    def post(self, request):
    #post is used for new user registration.
        serializer = UserSerializer(data = request.data) #convert requested data into object through serializer
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status = 201) #sucess code
        return Response(serializer.errors, status = 400) #error code


class MyTokenObtainPairView(TokenObtainPairView): 
    serializer_class = MyTokenObtainPairSerializer 

    # to create new token ,, test api from following url : /myapi/users/login/
    # to refresh token go to /myapi/users/token/refresh/