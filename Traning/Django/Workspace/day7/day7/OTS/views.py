from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *
import random

# WELCOME PAGE
def welcome(request):
    template=loader.get_template('welcome.html')
    res=template.render()
    return HttpResponse(res)


# REGISTRATION PAGE
def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res




# CANDIDATE  REGISTERATION
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
         
         


# LOGIN PAGE
def loginView(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError="Invalid Username or Password"
            res=render(request,'login.html',{'loginError':loginError})
        else:
        #login Success
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
            res=render(request,'home.html')
            return(res)
    else:
        res=render(request,'login.html')
        return res
   



# HOME PAGE
def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponse('login')
        return(res)
    else:
        res=render(request,'home.html')
    return(res)



# TEST PAPER
def testPaper(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
        #fetch question from database table
    n=int(request.GET['n'])
    question_pool=list(Question.objects.all())
    random.shuffle(question_pool)
    questions_list=question_pool[:n]
    context={'questions':questions_list}
    res=render(request,'test_paper.html',context)
    return res



# CALCULATE TEST RESULT
def calculateTestResult(request):
    pass  


# RESULT HISTORY
def testResultHistory(request):
    pass  


# SHOW TEST RESULT
def showTestResult(request):
    pass



# LOGOUT PAGE
def logoutView(request):
    if 'name' in request.session.keys():
        del request.session['username']
        del request.session['name']
    return HttpResponseRedirect("login")

    

# Create your views here.
