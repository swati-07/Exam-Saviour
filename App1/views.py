from django.shortcuts import render,redirect
from .forms import Register
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Notes
from django.contrib.auth.models import User
from .forms import NotesUpload
from django.contrib.auth.decorators import login_required
# Create your views here.

def homeview(request):
	return render(request,'home.html',{})
@login_required
def dashboardview(request):
	notes=Notes.objects.all().filter(approved=True).order_by('-uploaded_at')
	return render(request,'dashboard.html',{'notes':notes})



@login_required
def dashboardfview(request):

	notes=Notes.objects.filter(approved=True).filter(user__userstatus='teacher').order_by('-uploaded_at')
	return render(request,'dashboard.html',{'notes':notes})

@login_required
def dashboardsview(request):

	notes=Notes.objects.filter(approved=True).filter(user__userstatus='student').order_by('-uploaded_at')
	return render(request,'dashboard.html',{'notes':notes})

@login_required
def profileview(request):
	profile=Profile.objects.get(user=request.user)
	if request.method=='POST':
		profile.user.username=request.POST['username']
		profile.user.first_name=request.POST['firstname']
		profile.user.last_name=request.POST['lastname']
		profile.branch=request.POST['branch']
		profile.institute=request.POST['institute']
		if bool(request.FILES.get('profilepicture', False)) == True:
			profile.profile_picture=request.FILES['profilepicture']
	
		profile.save()
		profile.user.save()
		return redirect('dashboard')

	return render(request,'profile.html',{'profile':profile})

 
@login_required
def notesuploadview(request):
	notes=NotesUpload()
	if request.method=='POST':
		notes=NotesUpload(request.POST,request.FILES)
		if notes.is_valid():
			object=notes.save(commit=False)
			object.name=str(request.user)
			profile=Profile.objects.get(user=request.user)
			object.user=profile
			object.save()
			return redirect('dashboard')
	return render(request,'notesupload.html',{'notes':notes})

@login_required
def myuploadsview(request):
	notes=Notes.objects.all().filter(user__user=request.user)
	return render(request,'myuploads.html',{'notes':notes})
@login_required
def deleteview(request,pk):
	note=Notes.objects.get(pk=pk)
	note.delete()
	return redirect('myuploads')
@login_required
def notesstatusview(request):
	notes_approved=Notes.objects.filter(user__user=request.user).filter(approved=True)
	notes_unapproved=Notes.objects.filter(approved=False)
	return render(request,'notesstatus.html',{'notes_app':notes_approved,'notes_unapp':notes_unapproved})

def registerview(request):
	form=Register()
	if request.method=='POST':
		form=Register(request.POST)
		if form.is_valid():
			form.save()
			userstatus=request.POST.get('userstatus')
			branch=request.POST.get('branch')
			username=request.POST.get('username')
			profile=Profile()
			profile.userstatus=userstatus
			profile.branch=branch
			profile.user=User.objects.get(username=username)
			profile.save()
			
			return redirect('home')
	return render(request,'register.html',{'form':form})

def loginview(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		try:
			login(request,user)
			return redirect('dashboard')
		except:
			return redirect('login')
	return render(request,'login.html',{})

def logoutview(request):
	logout(request)
	return redirect('home')
