from django.db import models

# Create your models here.
class item(models.Model):
    item_number=models.AutoField
    item_name=models.CharField(max_length=60,default="")
    desc=models.CharField(max_length=70,default="")
    found_date=models.DateField()
    item_pic=models.ImageField(upload_to="lostitems/images",default="")

    def __str__(self):
        return self.item_name