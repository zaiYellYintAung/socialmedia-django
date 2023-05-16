from django.db import models

# Create your models here.
class ContentType(models.Model):
	type=models.CharField(max_length=69)

class Post(models.Model):
	user=
