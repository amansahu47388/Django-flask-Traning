from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *
import random

def welcome(request):
    template = loader.get_template('welcome.html')
    res = template.render()
    return HttpResponse(res)


def candidateRegistrationForm(request):
    res = render(request,'registration_form.html')
    return res


def candidateRegistration(request):
   if request.method=='POST':
     username=request.POST['username']
    #Check if the user already exists
     if(len(Candidate.objects.filter(username=username))):
        userStatus=1
     else:
        candidate=Candidate()
        candidate.username=username
        candidate.password=request.POST['password']
        candidate.name=request.POST['name']
        candidate.save()
        userStatus=2
   else:
        userStatus=3 #Request method is not POST
   context={
          'userStatus':userStatus
    }
   res=render(request,'registration.html',context)
   return res

        

def loginView(request):
    res = render(request,'login.html')
    return res

def candidateHome(request):
    pass
def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass