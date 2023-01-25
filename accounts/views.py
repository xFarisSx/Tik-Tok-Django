from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms
from . import models

# Create your views here.
def register(request):
	
	if request.method == "POST":
		form = forms.Register(request.POST)
		if form.is_valid():
			user = form.save()
			profile = models.Profile.objects.create(user=user, image=request.FILES.get('photo'))
			login(request, user)

			return redirect('home')

	form = forms.Register()
	return render(request, 'register.html', {'form':form})
