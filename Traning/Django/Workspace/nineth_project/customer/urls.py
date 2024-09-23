from django.urls import path
from customer.views import *
app_name = 'customer'

urlpatterns = [
    path('home/', home),
    path('result/', result,name='result'),
]
