from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def login(request):
     return render(request,'dashboard/log.html')

def itemadd(request):
    return HttpResponse ("item is here")

def showallpost(request):
    return HttpResponse("there is show all post")