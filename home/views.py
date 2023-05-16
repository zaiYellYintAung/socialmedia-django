from django.shortcuts import render,redirect

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
	templates="home/index.html"

	data={
		"title":"Home"
	}

	return render(request,templates,data)

def about(request):
	templates="home/about.html"

	data={
		"title":"About"
	}

	return render(request,templates,data)

def signin(request):
	templates="home/signin.html"

	data={
		"title":"Sign in"
	}

	return render(request,templates,data)

def signout(request):
	templates="home/signout.html"

	data={
		"title":"Sign out"
	}

	return render(request,templates,data)


def register(request):
	templates="home/register.html"

	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(request,username=username,password=password)
			signin(request,user)
			messages.success(request,("Please login "))
			return redirect('loginpage')
		else:
			messages.success(request,("Not okay"))
			return redirect('registerpage')
	data={
		"title":"Register"
	}

	return render(request,templates,data)