from django.contrib import admin
from .models import Profile,Hobby,Friendship,Follower

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hobby)
admin.site.register(Friendship)
admin.site.register(Follower)
