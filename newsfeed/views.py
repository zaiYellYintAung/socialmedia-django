from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="{% url 'signinpage'%}")
def newsfeed(request):
	template="newsfeed/index.html"
	posts=Post.objects.all()

	data={
		"posts":posts
	}

	return render(request,template,data)

@login_required(login_url="{% url 'signinpage'%}")
def create(request):
	template="newsfeed/create_demo.html"
	if request.method =='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.save()
			return redirect('newsfeedpage')
		else:
			messages.success(request,"Not valid")
	else:
		form=PostForm()

	data={
		'form':form
	}

	return render(request,template,data)

@login_required(login_url="{% url 'signinpage'%}")
def detail(request,pk):
	template="newsfeed/details.html"
	post=Post.objects.get(id=pk)
	check=(request.user!=post.user)


	if request.method=='POST':
		comment=request.POST['comment-text']
		new_comment=Comment(user=request.user,text=comment,post=post)
		new_comment.save()

	data={
		'post':post,
		'check':check
	}

	return render(request,template,data)

@login_required(login_url="{% url 'signinpage'%}")
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

@login_required(login_url="{% url 'signinpage'%}")
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


@login_required(login_url="{% url 'signinpage'%}")
def delete_comment(request,pk):
	template="newsfeed/comment_delete.html"
	comment=Comment.objects.get(id=pk)
	comment_origin=comment.post.id
	if request.method=='POST':
		if request.user==comment.user:
			comment.delete()
			messages.success(request,"Comment Deleted!!")
			return redirect(f'/newsfeed/detail/{comment_origin}')

	data={

	}

	return render(request,template,data)


