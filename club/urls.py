from django.contrib import admin
from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.club, name="ClubsHome"),
    path("group/<int:myid>", views.clubdesc, name="ClubDesc"),
    path('clubnotices/', views.clubnotices, name="ClubNotices")
    ]