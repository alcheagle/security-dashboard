"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from scanner import models

def show_start_page (request):
    return (HttpResponse((loader.get_template("index.html")).render(None, request)))

def query_mongo_per_coglioni (domain):
    pass

def get_url (request):
    if request.method=='POST':
        pass
        # try url=request.POST.get('url_field'):
        #
        # except Exception:
        #     return HttpResponse("Url field empty")
    else:
        return HttpResponse("Bad transition method")

urlpatterns = [
    url(r'^', show_start_page),
]
