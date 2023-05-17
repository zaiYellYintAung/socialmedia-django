from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Hobby(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Topic(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hobbies = models.ManyToManyField(Hobby)
    profile_photo = models.ImageField(null=True, blank=True)
    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    topic = models.ManyToManyField(Topic)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class React(models.Model):
    REACT_TYPES = (
        ("Like", "Like"),
        ("Love", "Love"),
        ("Wow", "Wow"),
        ("Funny", "Funny"),
        ("Awesome", "Awesome")
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    react = models.CharField(max_length=10, choices=REACT_TYPES)
    created = models.DateTimeField(auto_now_add=True)


class Friendship(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='friendships_sent', on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, related_name='friendships_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.user.username} is following {self.following.user.username}'
