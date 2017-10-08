# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from scanner import models
import os, json, string

def show_start_page (request):
    return (HttpResponse((loader.get_template("index.html")).render(None, request)))

def query_mongo_per_coglioni (domain):
    CD=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(CD, "input.json")) as json_data:
        return json.load(json_data)


def get_url (request):
    if request.method == 'GET':
        url=request.GET['site']
        urls=url.split(',')
        print(urls)
        PYTHON_DICTIONARY=query_mongo_per_coglioni(None)
        return JsonResponse(PYTHON_DICTIONARY)
    else:
        return HttpResponse("Bad transition method")
