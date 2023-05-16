from django.shortcuts import render

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

	data={
		"title":"Register"
	}

	return render(request,templates,data)