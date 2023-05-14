from rest_framework import serializers
from .models import Post #post imported from models 
class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username') 
    #the username will be current authorized user i,e user.username
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'user', 'hashtags')
