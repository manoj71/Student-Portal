from django.shortcuts import render
from .models import Contactcomplain, Contactenquiry
from home.views import getk
def cne(request):
    thank  = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        querytype = request.POST.get('querytype', '')
        query_status = request.POST.get('query_status', '')
        querysub = request.POST.get('querysub', '')
        branchyear = request.POST.get('branchyear', '')
        querydesc = request.POST.get('querydesc', '')
        email = request.POST.get('email', '')
        rollnumber =getk(request)
        phone = request.POST.get('phone', '')
        complain = Contactcomplain(name=name, email=email,
                                   rollnumber=rollnumber,branchyear=branchyear, phone=phone,querytype=querytype,
                                   querydesc=querydesc,query_status="Pending",querysub=querysub)
        if complain.querytype== "COMPLAIN":
            thank = True
            complain.save()


        enquiry = Contactenquiry(name=name, email=email,
                                   rollnumber=rollnumber,branchyear=branchyear, phone=phone,querytype=querytype,
                                   querydesc=querydesc,query_status="Pending",querysub=querysub )
        if querytype== "ENQUIRY":
            thank = True
            enquiry.save()

    return render(request, 'cne.html',{'thank': thank})
