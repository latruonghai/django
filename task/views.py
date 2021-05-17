from django.shortcuts import render
from .models import ToDoList, Item

from django.http import HttpResponse

def index(response, name):
    t = ToDoList(name = "User {}".format(name))
    t.save()
    return HttpResponse("<h1>{} </h1>".format(ToDoList.objects.get(name = "User {}".format(name))))

def v1(response):
    return HttpResponse("<h1> Hello Hai</h1>")


