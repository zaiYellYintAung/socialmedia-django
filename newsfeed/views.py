from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def newsfeed(request):
	template="newsfeed/index.html"
	posts=Post.objects.all()

	data={
		"posts":posts
	}

	return render(request,template,data)

def create(request):
	template="newsfeed/create.html"

	if request.method=='POST':
		messages.success(request,"Post created!!")
		return redirect('newsfeedpage')

	data={

	}

	return render(request,template,data)

def detail(request,pk):
	template="newsfeed/details.html"

	data={

	}

	return render(request,template,data)

def edit(request,pk):
	template="newsfeed/edit.html"

	if request.method=='POST':
		messages.success(request,"Post Edited!!")
		return redirect('newsfeedpage')

	data={

	}

	return render(request,template,data)

def delete(request,pk):
	template="newsfeed/delete.html"
	if request.method=='POST':
		messages.success(request,"Post Deleted!!")
		return redirect('newsfeedpage')

	data={

	}

	return render(request,template,data)

