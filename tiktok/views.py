from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.
@login_required(redirect_field_name='login')
def home(request):
	videos = models.Video.objects.all()[::-1][0:11]
	if request.method == 'GET':
		video = request.GET['video']
		print(video)
	return render(request, 'main/home.html', {'videos':videos})

@login_required(redirect_field_name='login')
def create(request):
	if request.method == 'POST':
		form = forms.UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			instance = models.Video(file=request.FILES['file'], title=request.POST['title'], user=request.user, songname=request.POST['songname'])
			instance.save()
			handle_uploaded_file(request.FILES['file'])
			return redirect('home')

	else:
		form = forms.UploadFileForm()

	return render(request, 'main/create.html', {
		'form':form
	})

def handle_uploaded_file(f):
	pass
    # with open(f.name, 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)

def redirectHome(request):
	return redirect('home/')