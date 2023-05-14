from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model): #Model for post
    user = models.ForeignKey(User, on_delete = models.CASCADE) #FK reference to default user model
    # on_delete = models.CASCADE means if user is deleted , post will be deleted
    title = models.CharField(max_length = 150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    hashtags = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
    #name the post object with the title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})
    #generate url based on primary key , 
