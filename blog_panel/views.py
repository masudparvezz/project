from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def sign(request):
    return render(request,'blog/sign.html')

def home_rent(request):
    return render(request,'blog/home_rent.html')

def shop_rent(request):
    return render(request,'blog/shop_rant.html')

def flat_sale(request):
    return render(request,'blog/flat_sale.html')