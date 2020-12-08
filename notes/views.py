from django.shortcuts import render
from .models import NoteSubject, DAANotes, DSDNotes
from math import ceil
from home.views import getk

def notes(request):
    allProds = []
    catprods = NoteSubject.objects.values('notes_subject', 'id')
    cats = {item['notes_subject'] for item in catprods}
    for cat in cats:
        prod = NoteSubject.objects.filter(notes_subject=cat)
        n = len(prod)
        allProds.append([prod, range(1, n)])
    params = {'allProds':allProds}
    user=getk(request)
    if user is not None:
        return render(request, 'notes/notes.html',params)
    else:
        return render(request,'log2home.html')    
    

def DAA(request):
    allProds = []
    catprods = DAANotes.objects.values('notes_name', 'id')
    cats = {item['notes_name'] for item in catprods}
    for cat in cats:
        prod = DAANotes.objects.filter(notes_name=cat)
        n = len(prod)
        allProds.append([prod, range(1, n)])
    params = {'allProds':allProds}
    return render(request, 'notes/notes2.html',params)


def DSD(request):
    allProds = []
    catprods = DSDNotes.objects.values('notes_name', 'id')
    cats = {item['notes_name'] for item in catprods}
    for cat in cats:
        prod = DSDNotes.objects.filter(notes_name=cat)
        n = len(prod)
        allProds.append([prod, range(1, n)])
    params = {'allProds':allProds}
    return render(request, 'notes/notes2.html', params)