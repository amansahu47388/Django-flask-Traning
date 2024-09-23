from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from store.models import *



def home(request):
    return render(request, 'home.html')



def Storebook(request):
    if request.method=='POST':
        bookstore=BookStore()
        bookstore.book_name=request.POST['bookname']
        bookstore.price=request.POST['price']
        bookstore.save()
        return render(request, 'home.html')
    return render(request, 'store_book.html')


def Getbook(request):
    book_pool=list(BookStore.objects.all())
    book_list=book_pool
    context={'books':book_list}
    return render(request, 'get_book.html',context)


# Create your views here.
