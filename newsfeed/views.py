from django.shortcuts import render, redirect
from .models import Post, Comment ,Topic
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="signinpage")
def newsfeed(request):
    template = "newsfeed/index.html"
    posts = Post.objects.all()

    data = {
        "posts": posts
    }

    return render(request, template, data)

@login_required(login_url="signinpage")
def create(request):
    template = 'newsfeed/create.html'

    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        topic_id = request.POST.get('topic')
        user = request.user

        post = Post.objects.create(title=title, text=text, image=image, user=user)
        post.topic.add(topic_id)
        return redirect('newsfeedpage')

    topics = Topic.objects.all()
    data = {'topics': topics}
    return render(request, template, data)
    

@login_required(login_url="signinpage")
def detail(request, pk):
    template = "newsfeed/details.html"
    post = Post.objects.get(id=pk)
    check = (request.user != post.user)

    if request.method == 'POST':
        comment = request.POST.get('comment-text')
        new_comment = Comment(user=request.user, text=comment, post=post)
        new_comment.save()

    data = {
        'post': post,
        'check': check
    }

    return render(request, template, data)


@login_required(login_url="signinpage")
def edit(request, pk):
    template = "newsfeed/edit.html"
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited successfully")
            return redirect('newsfeedpage')
    else:
        form = PostForm(instance=post)

    data = {
        "form": form,
        "post": post
    }

    return render(request, template, data)


@login_required(login_url="signinpage")
def delete(request, pk):
    template = "newsfeed/delete.html"
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect('newsfeedpage')

    data = {}

    return render(request, template, data)


@login_required(login_url="signinpage")
def delete_comment(request, pk):
    template = "newsfeed/comment_delete.html"
    comment = Comment.objects.get(id=pk)
    comment_origin = comment.post.id

    if request.method == 'POST':
        if request.user == comment.user:
            comment.delete()
            messages.success(request, "Comment deleted successfully")
            return redirect(f'/newsfeed/detail/{comment_origin}')

    data = {}

    return render(request, template, data)
