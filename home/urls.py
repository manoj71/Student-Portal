from django.urls import path
from . import views 


urlpatterns=[
     path('',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('loghome/',views.loghome,name='home'),
     path('loghome/logout',views.loghome),
     #path('home/',views.loghome),
     path('hme/',views.hme)
 ]