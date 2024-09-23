from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    s = "<h1>Hello & welcome to my first project</h1>" 
    return HttpResponse(s)


def myclass(request):
    v = "<marquee><h2>This is my AI&DS Class</h2></marquee>"
    return HttpResponse(v)



# Create your views here.
