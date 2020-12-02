from django.shortcuts import render
from .models import item
# Create your views here
def lost_items(request):
    if request.method=='POST':
        itm=item()
        itm.item_name=request.POST.get('item_name')
        itm.desc=request.POST.get('desc')
        itm.found_date=request.POST.get('found_date')
        itm.item_pic=request.POST.get('item_pic')
        itm.save()
        items=item.objects.all()

        return render(request,'lost_items_section.html',{'items':items})

    else:
        items=item.objects.all()
        return render(request,'lost_items_section.html',{'items':items})
