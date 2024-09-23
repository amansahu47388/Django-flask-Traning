from django.urls import path
from shoping_website import views
urlpatterns = [
    path('',views.home),
    path('contect/',views.contect),
    path('about/',views.about),
    
]
