"""test_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from demo_app2 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path("",views.home),
    path("bound_box",views.bound_box,name='bound_box'),
    path("bounding",views.bounding,name='bounding'),
    path("contact",views.contact,name='contact'),
    path("login",views.loginUser,name="login"),
    path("logout",views.logout,name="logout"),  
    path("hello",views.pdf_get,name='pdf'),
    path("file",views.upload,name='upload'),
    path ("index",views.index,name='index'),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



    