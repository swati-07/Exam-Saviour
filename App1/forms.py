from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notes

class Register(UserCreationForm):

	class Meta:
		model= User
		fields=['username','password1','password2','email','first_name','last_name']

class NotesUpload(ModelForm):

	class Meta:
		model=Notes
		fields=['topic_name','description','notes']