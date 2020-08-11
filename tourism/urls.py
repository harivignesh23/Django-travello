from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    
    path('destination_details',views.destination_details, name='destination_details'),
    path('destination',views.destination, name='destination'), 
    path('elements', views.elements, name='elements'),
    path('blog',views.blog, name='blog'),
    path('singleblog',views.singleblog, name='singleblog')
]