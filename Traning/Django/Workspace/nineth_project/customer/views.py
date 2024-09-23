from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def result(request):
    cls=joblib.load('customermlmodel.sav')
    lis=[]
    lis.append(request.GET['ID'])  
    lis.append(request.GET['Visit.Time	'])  
    lis.append(request.GET['Average.Expense	'])  
    lis.append(request.GET['Sex'])  
    
    ans=cls.predict([lis])

    return render(request, 'result.html', {'ans':ans , 'lis':lis})
# Create your views here.
