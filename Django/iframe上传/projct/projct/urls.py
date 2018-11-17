"""projct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from app01 import  views
from  django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'index$',views.index),
    url(r'ajax1.html',views.ajax1),
    url(r'index1$',views.index1),
    url(r'ajax2.html',views.ajax2),
    url(r'putfile$',views.putfile),
    url(r'index2.html$',views.index2),
]
