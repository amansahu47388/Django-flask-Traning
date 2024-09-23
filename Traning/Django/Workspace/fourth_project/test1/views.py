from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que = "Who devloped python ?"
    a="denis Ritche"
    b="guide van rossum"
    c="aman"
    d="monu"
    context = {
        'que':que,
        'options':[a,b,c,d]
    }
    template = loader.get_template("test.html")
    res= template.render(context,request)
    return HttpResponse(res)



 # Create your views here.
