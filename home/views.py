from django.shortcuts import render
from .models import *

# Create your views here.6


def home(request):
    views = {}
    views['services'] = Service.objects.all()
    return render(request,'index.html',views)


def about(request):
    view = {}
    view['feedbacks'] = Feedback.objects.all()
    return render(request,'about.html',view)


def portfolio(request):
    return render(request,'portfolio.html')


def contact(request):
    stay = {}
    stay['informations'] = Information.objects.all()
    return render(request,'contact.html', stay)


def price(request):
    return render(request,'price.html')




def services(request):
    offer = {}
    offer['services']= Service.objects.all()
    return render(request,'services.html',offer)





