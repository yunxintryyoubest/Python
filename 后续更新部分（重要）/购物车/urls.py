"""购物车 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from   django.conf.urls  import url
from   app01 import views
from   app01 import  payment

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'index/$',views.index),
    url(r'^test/$',views.test),
    url(r'login/$',views.Login.as_view()),
    url(r'register/$',views.Register.as_view({'post':'register'})),
    # url(r'accountview/$',views.AccountView.as_view({'post':'create'})),
    url(r'accountview/$', views.AccountView.as_view()),
    url(r'shopping_car/$', views.shopping_car.as_view()),
    url(r'payment/$', payment.Payment_Viewset.as_view()),
    # url(r'^accountview/$', views.AccountView.as_view({'post': 'create','delete':'destroy'})),
]
