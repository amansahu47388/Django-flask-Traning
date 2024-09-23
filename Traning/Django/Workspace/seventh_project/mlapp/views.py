from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib


def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())


def result(request):
    cls=joblib.load('glassmlmodel.sav')
    lis=[]
    lis.append(request.GET['RI'])  
    lis.append(request.GET['Na'])  
    lis.append(request.GET['Mg'])  
    lis.append(request.GET['AI'])  
    lis.append(request.GET['Si'])  
    lis.append(request.GET['K'])  
    lis.append(request.GET['Ca'])  
    lis.append(request.GET['Ba'])  
    lis.append(request.GET['Fe'])  
   
    ans=cls.predict([lis])

    return render(request, 'result.html', {'ans':ans , 'lis':lis})



# Create your views here.
