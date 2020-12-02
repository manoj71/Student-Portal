from django.db import models

# Create your models here.
class item(models.Model):
    item_number=models.AutoField
    subject=models.CharField(max_length=60,default="")
    topic=models.CharField(max_length=70,default="")
    
    pic=models.ImageField(upload_to="notes/images",default="")
    pdf_file=models.FileField(upload_to="notes/pdf", max_length=100)


    def __str__(self):
        return self.topic