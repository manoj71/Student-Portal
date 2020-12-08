from django.db import models

# Create your models here.
class student(models.Model):
    roll_number=models.BigIntegerField()
    student_name=models.CharField(max_length=50)
    Subject_1=models.CharField(max_length=40)
    Subject_1_marks=models.IntegerField(default=0)
    Subject_2=models.CharField(max_length=40)
    Subject_2_marks=models.IntegerField(default=0)
    Subject_3=models.CharField(max_length=40)
    Subject_3_marks=models.IntegerField(default=0)
    Subject_4=models.CharField(max_length=40)
    Subject_4_marks=models.IntegerField(default=0)
    Subject_5=models.CharField(max_length=40)
    Subject_5_marks=models.IntegerField(default=0)
    marksheet=models.FileField(upload_to="exams/marksheet",default="",blank=True)

    def __str__(self):
        return self.student_name