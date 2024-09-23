from django.shortcuts import render
from django.http import HttpResponse

def testpaper(request):
    s= "This is a test paper"
    return HttpResponse(s)

def resultpage(request):
    s= "This is a result  page"
    return HttpResponse(s)

# Create your views here.
