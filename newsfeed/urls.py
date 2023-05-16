from django.urls import path

urlpatterns=[
	path('',views.newsfeed,name="newsfeedpage"),
	path('create/',views.create,name="createpage"),
	path('detail/<int:pk>',views.detail,name="detailpage"),
	path('edit/<int:pk>',views.edit,name="editpage"),
	path('delete/<int:pk>',views.delete,name="deletepage"),
]