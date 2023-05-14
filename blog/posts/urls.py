from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, UserPostAPIView

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('<username>/', UserPostAPIView.as_view())
]