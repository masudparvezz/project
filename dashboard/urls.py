from django.urls import path
from . import views
 
urlpatterns=[
    
    path('login',views.bloglogin,name='login'),
    path('logout',views.bloglogout, name='logout'),
    path('',views.dashboard,name='dashboard'),
    path('home_rent',views.home_rent,name='home_rent'),
    path('flat',views.flat,name='flat'),
    path('shop_rent',views.shop_rent,name='shop_rent'),
    path('setting',views.setting,name='setting')
]