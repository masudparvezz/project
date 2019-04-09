from django.urls import path
from . import views
 
urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('login',views.login,name='login'),
    path('itemadd',views.itemadd,name='itemadd'),
    path('showallpost',views.showallpost,name='showallpost'),
    path('setting',views.setting,name='setting')
]