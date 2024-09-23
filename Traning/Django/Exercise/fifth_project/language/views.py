from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def python(request):
    template = loader.get_template("python.html")
    res = template.render()
    return HttpResponse(res)


def c(request):
    template = loader.get_template("c.html")
    res = template.render()
    return HttpResponse(res)

def cpp(request):
    template = loader.get_template("c++.html")
    res = template.render()
    return HttpResponse(res)


def java(request):
    template = loader.get_template("javascript.html")
    res = template.render()
    return HttpResponse(res)

def ml(request):
    template = loader.get_template("ml.html")
    res = template.render()
    return HttpResponse(res)