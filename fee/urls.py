from django.contrib import admin
from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.fee, name="FeeHome"),
    path("FP/", views.semfee, name="SemHome"),
    path("FP/checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest")
    ]