from django.urls import path
from . import views 


urlpatterns=[
     path('',views.home,name='h'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     
 ]