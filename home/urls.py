from django.urls import path
from . import views

urlpatterns=[
	path("",views.index,name="homepage"),

	path("home/",views.index,name="homepage"),
	path("about/",views.about,name="aboutpage"),
	path("profile/<int:pk>",views.profile,name="profilepage"),
	path("signin/",views.signin,name="signinpage"),
	path("signout/",views.signout,name="signoutpage"),
	path("register/",views.register,name="registerpage"),

]
