from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
		
	class Meta:
		model=Post
		fields=['title','text','image','topic']


