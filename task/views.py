from django.shortcuts import render

from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1> Hello </h1>")

def v1(response):
    return HttpResponse("<h1> Hello Hai</h1>")
# Create your views here.
