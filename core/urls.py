"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from App1.views import homeview,registerview,loginview,logoutview,dashboardview,profileview,deleteview,notesstatusview,notesuploadview,dashboardfview,myuploadsview,dashboardsview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeview,name='home'),
    path('register/',registerview,name="register"),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    path('dashboard/',dashboardview,name='dashboard'),
    path('notes/upload/',notesuploadview,name='notesupload'),
    path('dashboard/faculty',dashboardfview,name='dashboardfaculty'),
    path('dashboard/student',dashboardsview,name='dashboardstudent'),
    path('myprofile/',profileview,name='myprofile'),
    path('myuploads/',myuploadsview,name='myuploads'),
    path('notestatus/',notesstatusview,name='notesstatus'),
    path('delete/<pk>/',deleteview,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,                       # This is important for media like photos and videos
                          document_root=settings.MEDIA_ROOT)
