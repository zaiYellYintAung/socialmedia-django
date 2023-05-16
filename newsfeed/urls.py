from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('',views.newsfeed,name="newsfeedpage"),
	path('create/',views.create,name="createpage"),
	path('detail/<int:pk>',views.detail,name="detailpage"),
	path('edit/<int:pk>',views.edit,name="editpage"),
	path('delete/<int:pk>',views.delete,name="deletepage"),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)