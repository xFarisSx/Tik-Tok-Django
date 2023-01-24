from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.redirectHome),
	path('home/', views.home,name='home'),
	path('create/', views.create,name='create'),
	path('like/', views.like, name='like'),
	path('comment/<int:id>', views.comment, name='comment'),
	path('profile/<int:id>', views.profile, name="profile"),
	path('video/<int:id>', views.video, name="video"),
	path('search/', views.search, name="search")
]
