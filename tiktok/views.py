from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='login')
def home(request):
	return render(request, 'main/home.html')

def redirectHome(request):
	return redirect('home/')