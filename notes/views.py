from django.shortcuts import render
from .models import item
# Create your views here.
def notes(request):
    items=item.objects.all()
    return render(request,'notes.html',{'items':items})