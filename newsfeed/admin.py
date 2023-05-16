from django.contrib import admin
from .models import Hobby, Topic, Profile, Post, Comment, React, Friendship, Follower

admin.site.register(Hobby)
admin.site.register(Topic)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(React)
admin.site.register(Friendship)
admin.site.register(Follower)