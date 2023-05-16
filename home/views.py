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

	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"Signed in")

			return redirect('homepage')


		else:
			messages.success(request,"Error!!")
			return redirect('signinpage')


	data={
		"title":"Sign in"
	}

	return render(request,templates,data)

# def login_user(request):
# 	data={}

# 	if request.method == "POST":
# 		username=request.POST['username']
# 		password=request.POST['password']
# 		user=authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request,user)
# 			return redirect('about')

# 		else:
# 			messages.success(request,("There is an error logging in "))
# 			return redirect('loginpage')
			

# 	else:	
# 		return render(request,"members/login.html",data)


def signout(request):
	templates="home/signout.html"
	if request.method=="POST":
		logout(request)
		messages.success(request,"Successfully signed out")
		return redirect('homepage')

	data={
		"title":"Sign out"
	}

	return render(request,templates,data)


def register(request):
	templates="home/register.html"

	form=UserCreationForm()
		# form.fields['username'].widget.attrs.update({'class': 'form-control'})
	 	# form.fields['password1'].widget.attrs.update({'class': 'form-control'})
	 	# form.fields['password2'].widget.attrs.update({'class': 'form-control'})


	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# username=form.cleaned_data['username']
			# password=form.cleaned_data['password1']
			# user=authenticate(request,username=username,password=password)
			# login(request,user)
			messages.success(request,("Please login "))
			return redirect('signinpage')
		else:
			form=UserCreationForm()
			messages.success(request,("Not okay"))
			return redirect('registerpage')

	data={
		"title":"Register",
		"form":form
	}

	return render(request,templates,data)

def profile(request):
	templates="home/profile.html"

	data={

	}
	return render(request,templates,data)