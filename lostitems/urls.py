from django.urls import path
from.import views

urlpatterns=[
     path('',views.lost_items,name='lost_items')
 ]