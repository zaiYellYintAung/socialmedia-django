from django.shortcuts import render,redirect

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm

###get data from newsfeed


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




@login_required(login_url="{% url 'signinpage'%}")
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
	if request.method=="POST":
		form=SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			username=request.POST['username']
			password=request.POST['password1']
			user=authenticate(request,username=username,password=password)

			if user is not None:
				login(request,user)
				new_profile=Profile(user=user,uid=user.id)
				new_profile.save()
				messages.success(request,("Please login "))
				logout(request)

				redirect('homepage')

		else:
			form=SignUpForm()
			messages.success(request,("Not okay"))
			return redirect('registerpage')

	else:
		form=SignUpForm()
	data={
		"title":"Register",
		"form":form
	}

	return render(request,templates,data)

@login_required(login_url="{% url 'signinpage'%}")
def profile(request,pk):
	profile=Profile.objects.get(uid=pk)
	toggle_follow_setting=request.user==profile.user

	follower=request.user
	following=User.objects.get(id=pk)
	li=Follower.objects.all()

	def checking(following,follower):
		if follower!=following:
			for obj in li:
				messages.success(request,f"follower {obj.follower.username},following {obj.following.username}")
				if follower==obj.follower and following==obj.following:
					messages.success(request,"Not Followed")
					return True
				else:
					messages.success(request,"Followed")
					
					return False

		elif follower==following:
			messages.success(request,"User")


	followed=checking(following,follower) 

	templates="home/profile.html"

	data={
		"profile":profile,
		"toggle_follow_setting":toggle_follow_setting,
		"followed":followed

	}
	return render(request,templates,data)



@login_required(login_url="{% url 'signinpage'%}")
def follow(request,pk):
	follower=request.user
	following=User.objects.get(id=pk)

	follow_list=Follower.objects.all()
	for obj in follow_list:
		if obj.follower != follower and obj.following != following:
			flw=Follower(follower=follower,following=following)
			flw.save()
			messages.success(request,f"Followed {following.username}")
			return redirect(f'profile/{following.username}')
		else:
			messages.success("??")
			return redirect(f'profile/{following.username}')

	return redirect(f'homepage')

@login_required(login_url="{% url 'signinpage'%}")
def unfollow(request,pk):
	follower=request.user
	following=User.objects.get(id=pk)

	follow_list=Follower.objects.all()
	for obj in follow_list:
		if obj.follower != follower and obj.following != following:
			flw=Follower(follower=follower,following=following)
			flw.save()
			messages.success(request,f"Followed {following.username}")
			return redirect(f'profile/{following.username}')
		else:
			messages.success("??")
			return redirect(f'profile/{following.username}')

	return redirect(f'homepage')


@login_required(login_url="{% url 'signinpage'%}")
def setting(request,pk):


	templates="home/setting.html"

	data={

	}
	return render(request,templates,data)
