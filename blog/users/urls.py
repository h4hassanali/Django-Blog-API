from django.urls import path
from .views import UsersAPIView #import usersapiview
from .views import UsersAPIView
from users.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('', UsersAPIView.as_view()), # mapped to userapiview in view.py file
     path('login/', MyTokenObtainPairView.as_view()), #to get token 
    path('token/refresh/', TokenRefreshView.as_view()), #to refresh a token using refresh token
]

#Working of access and refresh token:
# Client send request for token and get two tokens 
# 1. Access token 
# 2. Refresh token
# After some period of time access token expires
# then user go to /token/refresh and provide refresh token.
# His access token is then refreshed , now he can perform specified operations
# with that access token