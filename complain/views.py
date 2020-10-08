from django.shortcuts import render

# Create your views here.
def complain(request):
    return render(request,'complaints_enquiry.html')