from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignUpForm
from newsfeed.models import Post


def index(request):
    template_name = "home/index.html"
    data = {"title": "Home"}
    return render(request, template_name, data)


def about(request):
    template_name = "home/about.html"
    data = {"title": "About"}
    return render(request, template_name, data)


def signin(request):
    template_name = "home/signin.html"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Signed in")
            return redirect("homepage")
        else:
            messages.error(request, "Error occurred while signing in")
            return redirect("signinpage")

    data = {"title": "Sign in"}
    return render(request, template_name, data)


@login_required(login_url="signinpage")
def signout(request):
    template_name = "home/signout.html"
    if request.method == "POST":
        logout(request)
        messages.success(request, "Successfully signed out")
        return redirect("homepage")

    data = {"title": "Sign out"}
    return render(request, template_name, data)


def register(request):
    template_name = "home/register.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                new_profile = Profile(user=user, uid=user.id)
                new_profile.save()
                messages.success(request, "Please login")
                logout(request)
                return redirect("homepage")
        else:
            form = SignUpForm()
            messages.error(request, "Invalid form submission")
            return redirect("registerpage")
    else:
        form = SignUpForm()
    data = {"title": "Register", "form": form}
    return render(request, template_name, data)


@login_required(login_url="signinpage")
def profile(request, pk):
    profile = Profile.objects.get(uid=pk)
    toggle_follow_setting = request.user == profile.user
    follower_user = request.user
    following_user = User.objects.get(id=pk)
    follow_exists = Follower.objects.filter(following=following_user, follower=follower_user).exists()
    posts = Post.objects.filter(user=request.user)
    template_name = "home/profile.html"
    data = {
        "profile": profile,
        "toggle_follow_setting": toggle_follow_setting,
        "followed": follow_exists,
        "posts": posts,
    }
    return render(request, template_name, data)


@login_required(login_url="signinpage")
def follow(request, pk):
    follower_user = request.user
    following_user = User.objects.get(id=pk)
    follow_exists = Follower.objects.filter(following=following_user, follower=follower_user).exists()

    if follow_exists:
        fol_delete = Follower.objects.get(following=following_user, follower=follower_user)
        fol_delete.delete()
        messages.success(request, f"Unfollowed {following_user.username}")
    else:
        Follower.objects.create(following=following_user, follower=follower_user)
        messages.success(request, f"Followed {following_user.username}")

    return redirect("profilepage", following_user.id)


@login_required(login_url="signinpage")
def setting(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        if "profile_picture" in request.FILES:
            profile.profile_photo = request.FILES["profile_picture"]

        if "bio" in request.POST:
            profile.bio = request.POST["bio"]

        if "hobby" in request.POST:
            hobbies = request.POST.getlist("hobby")
            profile.hobbies.set(hobbies)

        profile.save()

    data = {"profile": profile}
    return render(request, "home/setting.html", data)
