from django.shortcuts import render
from .models import *

# Create your views here.6


def home(request):
    views = {}
    views['services'] = Service.objects.all()
    return render(request,'index.html',views)


def about(request):
    return render(request,'about.html')


def portfolio(request):
    return render(request,'portfolio.html')


def contact(request):
    return render(request,'contact.html')


def price(request):
    return render(request,'price.html')




def services(request):
    return render(request,'services.html')





