from django.urls import path
from store.views import *
app_name='store'
urlpatterns = [
    path('',home),
    path('storebook',Storebook, name='StoreBook'),
    path('getbook', Getbook, name='GetBook')
]