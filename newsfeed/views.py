from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *

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
	post_form=PostForm()
	topic=Topic.objects.all()
	if request.method=='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Post created!!")
			return redirect('newsfeedpage')
		else:
			messages.success(request,"Try again!")
			return redirect('createpage')

	data={
		"form":post_form,
		"topics":topic,
	}

	return render(request,template,data)

def detail(request,pk):
	template="newsfeed/details.html"
	post=Post.objects.get(id=pk)
	data={
		'post':post
	}

	return render(request,template,data)

def edit(request,pk):
	template="newsfeed/edit.html"
	post=Post.objects.get(id=pk)
	form=PostForm(instance=post)

	if request.method=='POST':
		form=PostForm(request.POST,instance=post)
		form.save()
		messages.success(request,"Post Edited!!")
		return redirect('newsfeedpage')

	data={
		"post":post
	}

	return render(request,template,data)

# def edit(request,pk):
# 	template="blogs/edit.html"
# 	project=Blogs.objects.get(id=pk)
# 	form=BlogForm(instance=project)

# 	if request.method=='POST':
# 		form =BlogForm(request.POST,instance=project)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('blogs')


def delete(request,pk):
	template="newsfeed/delete.html"
	post=Post.objects.get(id=pk)

	if request.method=='POST':
		post.delete()
		messages.success(request,"Post Deleted!!")
		return redirect('newsfeedpage')

	data={

	}

	return render(request,template,data)

