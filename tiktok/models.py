from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, default=None)
    file = models.FileField(null=False, upload_to="videos")
    # validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])]
    songname = models.CharField(max_length=255, null=False, default='No song')

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete= models.CASCADE)
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete= models.CASCADE)
    comment = models.CharField(null=False, max_length=250)

class CommentLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)