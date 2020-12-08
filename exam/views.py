from django.shortcuts import render
from .models import student
# Create your views here.
def exams(request):
    #request.session['user']=11911071
    #user=request.session.get('user')
    #user=getk(request)
    #if(user==None):
      #user=11911076

    #del request.session['user']
    stud=student.objects.get(roll_number__exact=11911076)
    studs=student.objects.filter(roll_number=11911073).values('Subject_1','Subject_1_marks')
    stud_subj={
        "subject_1":stud.Subject_1,
        "subject_2":stud.Subject_2,
        "subject_3":stud.Subject_3,
        "subject_4":stud.Subject_4,
        "subject_5":stud.Subject_5
    }
    stud_marks={
        "subject_1_marks":stud.Subject_1_marks,
        "subject_2_marks":stud.Subject_2_marks,
        "subject_3_marks":stud.Subject_3_marks,
        "subject_4_marks":stud.Subject_4_marks,
        "subject_5_marks":stud.Subject_5_marks
    }
    return render(request,'exams_marks.html',{'student':stud,'stud_subj':stud_subj,'stud_marks':stud_marks})