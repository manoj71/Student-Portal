from django.shortcuts import render
from .models import Group, Groupnotices
from math import ceil


def club(request):
    allProds = []
    catprods = Group.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Group.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides)])
    params = {'allProds':allProds}
    return render(request, 'club/clubs.html',params)

def clubnotices(request):
    allProds = []
    catprods = Groupnotices.objects.values('notice_category', 'id')
    cats = {item['notice_category'] for item in catprods}
    for cat in cats:
        prod = Groupnotices.objects.filter(notice_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'club/clubnotices.html', params)

def clubdesc(request, myid):

    # Fetch the product using the id
    group = Group.objects.filter(id=myid)
    return render(request, 'club/clubsdesc.html', {'group':group[0]})