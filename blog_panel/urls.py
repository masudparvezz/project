from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='home'),
    path('sign',views.sign, name='sign'),
    path('home_rent', views.home_rent, name='home_rent'),
    path('shop_rant',views.shop_rent,name='shop_rant'),
    path('flat_sale',views.flat_sale, name='flat_sale')
]