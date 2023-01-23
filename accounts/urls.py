from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from . import forms

urlpatterns = [
	path('login/', LoginView.as_view(authentication_form = forms.UserLoginForm), name='login'),
	path("", include("django.contrib.auth.urls")),
	path('register/', views.register, name="register")
]
