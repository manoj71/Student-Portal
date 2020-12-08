from django.db import models

# Create your models here.
class studentid(models.Model):
    student_name=models.CharField(max_length=50,default="")
    roll_num=models.BigIntegerField()
    password=models.CharField(max_length=70,default="")

    def authenticate(roll,pwd):
        stud=studentid.objects.get(roll_num__exact=roll)
        if stud.password==pwd:
            if stud is not None:
                return stud
            else:
                return stud 
        else:
            return            
   
    def __str__(self):
        return self.student_name