from django.shortcuts import render,redirect
from .models import studentid
from django.contrib import messages
# Create your views here.
def login(request):
     request.session['user']=None
     if request.method=='POST':
        user_name=request.POST['rollnumber']
        pwd=request.POST['password']
        user=studentid.authenticate(roll=user_name,pwd=pwd)
        if user is not None:
            request.session['user']=user_name
            return render(request,'home.html')
        else:
            messages.info(request,'invalid')
            return render(request,'login.html')
     else:
        return render(request,'login.html')      
def hme(request):
    return render(request,'log2home.html')
def logout(request):
    del request.session['user']
    return render(request,'log2home.html')
    #return render(request,'login.html')       
def loghome(request): 
        return render(request,'home.html')
           
def getk(request):
    rl=request.session.get('user')
    return rl    

    