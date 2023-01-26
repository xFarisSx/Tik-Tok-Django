from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='profile_pics')

class Follower(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True)
    
class Following(models.Model):
    following = models.ForeignKey(User,on_delete=models.CASCADE,  null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,  null=True)
    