from django.shortcuts import render

# Create your views here.
def lost_items(request):
    return render(request,'lost_items_section.html')