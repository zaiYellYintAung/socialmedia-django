from django.contrib import admin
from .models import  Topic,  Post, Comment, React


admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(React)
