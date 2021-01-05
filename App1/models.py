from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_picture=models.ImageField(upload_to='media',blank=True,default='dp.jpg')
	userstatus=models.CharField(max_length=10)
	institute=models.CharField(max_length=200)
	branch=models.CharField(max_length=50)

class Notes(models.Model):
	user=models.ForeignKey(Profile,on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	topic_name=models.CharField(max_length=200)
	description=models.CharField(max_length=400,blank=True)
	notes=models.FileField()
	uploaded_at=models.DateTimeField(default=timezone.now)
	approved=models.BooleanField(default=False)
	