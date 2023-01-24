from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from . import models


# Create your views here.
@login_required(redirect_field_name='login')
def home(request):
	videos = models.Video.objects.all()[::-1][0:11]
	return render(request, 'main/home.html', {'videos':videos})

@login_required(redirect_field_name='login')
def profile(request, id):
	user = User.objects.get(id=id)
	return render(request, 'main/profile.html', {
		'user':user
	})

@login_required(redirect_field_name='login')
def search(request):
	q = request.GET.get('q')
	instead = ''
	if q:
		users = User.objects.filter(username__icontains=q)
		if not users:
			users = None
			instead = 'Not Found!'

	else : 
		users = None
		instead = 'Search'
	return render(request, 'main/search.html', {'users':users, 'instead':instead})

@login_required(redirect_field_name='login')
def video(request, id):
	video = models.Video.objects.get(id=id)
	return render(request, 'main/video.html', {
		'video':video
	})

@login_required(redirect_field_name='login')
def like(request):
	if request.method == 'GET':
		video_id = request.GET.get('video', False)
		if video_id:
			video = models.Video.objects.get(pk=video_id)
			like = video.like_set.filter(user=request.user)
			if like:
				like.delete()
			else:
				video.like_set.create(user=request.user, video=video)
				video.save()

	return redirect('home')
@login_required(redirect_field_name='login')
def comment(request, id):
	video=models.Video.objects.get(id=id)
	if request.method == "GET":
		comment_text = request.GET.get('text', False)
		if comment_text:
			video.comment_set.create(comment=comment_text, user=request.user, video=video)
			video.save()

	return render(request, 'main/comment.html', {
		'video':video
	})

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