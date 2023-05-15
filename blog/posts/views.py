from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User


# 1: Get list of all posts 

class PostListAPIView(APIView):  #Base class = APIView 
    permission_classes = [permissions.IsAuthenticated] #only authorized users can access this view

    def get(self, request, *args, **kwargs): #Get all posts
        posts = Post.objects.all() #Fetch all objects of post
        serializer = PostSerializer(posts, many = True) #serialize the data
        return Response(serializer.data, status = status.HTTP_200_OK) #return serialized data

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.pk,
            'title': request.data.get('title'),
            'body': request.data.get('body'),
            'hashtags': request.data.get('hashtags')
        }
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class PostDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response({'error': 'Post not found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data, status = status.HTTP_200_OK)

    


    def put(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response({'error': 'Post not found'}, status = status.HTTP_404_NOT_FOUND)
        data = {
            'user': request.user.id,
            'title': request.data.get('title'),
            'body': request.data.get('body'),
            'hashtags':request.data.get('hashtags')
        }
        serializer = PostSerializer(post, data = data, partial = True)
        if serializer.is_valid():
            if post.user.id == request.user.id:
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({"error": "You are not authorized to edit this post"}, status = status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response({'error': 'Post not found'}, status = status.HTTP_404_NOT_FOUND)
        if post.user.id == request.user.id:
            post.delete()
            return Response({"res": "Object deleted!"}, status = status.HTTP_200_OK)
        return Response({"error": "You are not authorized to delete this post"}, status = status.HTTP_401_UNAUTHORIZED)
    
class UserPostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

   
    def get(self, request, username, *args, **kwargs):
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        posts = Post.objects.filter(user=user)
        
        title = request.query_params.get('title')  # Get the 'title' query parameter from the URL
        if title:
            posts = posts.filter(title__icontains=title)  # Filter posts by title
        

        created = request.query_params.get('created')
        if created:
            created_date = parse_datetime(created)
            if created_date:
                posts = posts.filter(created=created_date)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
