from django.shortcuts import render
from .models import Destination
from .models import popular

# Create your views here.
def index(request):
    obs=Destination.objects.all()
    obps=popular.objects.all()
    return render(request, 'index.html', {'obs':obs ,'obps':obps})


def about(request):
    return render (request,'about.html')


def destination (request):
    obs=Destination.objects.all()
    obps=popular.objects.all()

    return render (request,'destination.html', {'obs':obs ,'obps':obps})


def destination_details(request):
    return render (request,'destination_details.html')

def elements(request):
    return render (request,'elements.html')

def blog(request):
    return render (request,'blog.html')

def singleblog(request):
    return render (request,'single-blog.html')

def contact(request):
    return render (request,'contact.html')




