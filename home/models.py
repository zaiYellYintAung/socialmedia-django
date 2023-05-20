
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User


class Hobby(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    hobbies = models.ManyToManyField(Hobby)
    profile_photo = models.ImageField(null=True, blank=True)
    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False, blank=True)
    uid=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username

class Friendship(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='friendships_sent', on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, related_name='friendships_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.username} is following {self.following.username}'
