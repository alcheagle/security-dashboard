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
from main_page import views as main_page_view
from mongo_model import  database
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def renderSitewithParam(request):
    template=loader.get_template("allDomains.html")

    lstHttps=database.getAllLatestToolProperty("PSHHT","Valid HTTPS")
    httpsTrue = 0
    for tpl in lstHttps:
        if tpl[1]=="true":
            httpsTrue +=1
    httpsFalse = len(lstHttps)-httpsTrue

    lstRedirect=database.getAllLatestToolProperty("PSHHT","Redirect")
    redirectTrue=0
    for tpl in lstRedirect:
        if tpl[1]=="true":
            redirectTrue +=1
    redirectFalse = len(lstRedirect)-redirectTrue


    lstSPF=database.getAllLatestToolProperty("PSHHT","Valid SPF")
    SPFTrue=0
    for tpl in lstSPF:
        if tpl[1]=="true":
            SPFTrue +=1
    SPFFalse = len(lstSPF)-SPFTrue

    lstMX=database.getAllLatestToolProperty("PSHHT","MX Record")
    MXTrue=0
    for tpl in lstMX:
        if tpl[1]=="true":
            MXTrue +=1
    MXFalse = len(lstMX)-MXTrue

    context = {
        'httpsTrue' : httpsTrue,
        'httpsFalse' : httpsFalse,
        'redirectTrue' : redirectTrue,
        'redirectFalse' : redirectFalse,
        'SPFTrue' : SPFTrue,
        'SPFFalse' : SPFFalse,
        'MXTrue' : MXTrue,
        'MXFalse' : MXFalse,
    }
    return (HttpResponse(template.render(context, requests)))



urlpatterns = [
    url(r'^allDomains', renderSitewithParam),
    url(r'^scan', main_page_view.get_url),
    url(r'^', main_page_view.show_start_page),

]
