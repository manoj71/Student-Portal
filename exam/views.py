from django.shortcuts import render

# Create your views here.
def exams(request):
    return render(request,'exams_marks.html')