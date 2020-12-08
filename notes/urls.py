from django.contrib import admin
from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.notes, name="NotesHome"),
    path('DSD/', views.DSD, name="DSDHome"),
    path('DAA/', views.DAA, name="DAAHome")
    ]