from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *
from .forms.flat import *
from .forms.shop import *
# Create your views here.



def bloglogin(request):
     if request.method == 'GET':
          return render(request,'dashboard/login.html')
     elif request.method == 'POST':
          username = request.POST.get('username',None)
          password = request.POST.get('password',None)
          user = authenticate(username=username,password=password)
          if user is not None:
               login(request,user)
               return HttpResponseRedirect(reverse('dashboard'))
          else:
               return HttpResponseRedirect(reverse('login'))

@login_required
def bloglogout(request):
    logout(request)
    context = {
        'message': 'Successfully Logout'
    }
    return render(request,'dashboard/login.html', context)

@login_required
def home_rent(request):
    return render (request,'dashboard/home_rent.html')


@login_required
def flat(request):
     if request.method == 'POST':
          form =FlatForm(request.POST)
          if form.is_valid():
               
               form.save()
          
               return render(request,'dashboard/flat_sale.html')
     else:
          form = FlatForm(request.GET)
          context = {
            'form' : form
        }
          return render(request, 'dashboard/flat_sale.html', context)

@login_required
def shop_rent(request):
     if request.method == 'POST':
          form = ShopForm(request.POST)
          form.save()
          return render(request,'dashboard/shop_rent.html')
     else:
          form = ShopForm(request.GET)
          shop_data = shop.object.all()
          context = {
               'shop_data': shop_data,
               'form' : form
          }
          return render(request, 'dashboard/shop_rent.html')



@login_required
def setting(request):
     return HttpResponse("i am setting")


@login_required
def dashboard(request):
    return render(request,'dashboard/dashboard.html')