# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from scanner import models
import os, json, string

def show_start_page (request): #Render home page
    return (HttpResponse((loader.get_template("index.html")).render(None, request)))

def query_mongo_per_coglioni (domain): #Mokc-up of a query
    CD=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(CD, "input.json")) as json_data:
        return json.load(json_data)


def get_url (request): #Query the database for a certain
    print ("COGLIONE")
    if request.method == 'GET':
        url=request.GET['site']
        urls=url.split(',')
        print(urls)
        PYTHON_DICTIONARY=query_mongo_per_coglioni(None)
        if not PYTHON_DICTIONARY:
            return JsonResponse(PYTHON_DICTIONARY)
        else:
            return HttpResponse("No data found for urls")
    else:
        return HttpResponse("Bad transition method")
