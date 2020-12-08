from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

class Group(models.Model):
    group_id=models.AutoField
    group_name=models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=300, default="")
    detaileddesc = models.CharField(max_length=300, default="")
    coordinator=models.CharField(max_length=300, default="")
    image= models.ImageField(upload_to="clubs/images",null=True, blank=True)
    pub_date = models.DateTimeField(null=True)
    document = models.FileField(upload_to="clubs/images",null=True, blank=True)


    def __str__(self):
        return self.group_name



class Groupnotices(models.Model):
    notice_id=models.AutoField
    notice_name=models.CharField(max_length=50, default="")
    notice_category = models.CharField(max_length=50, default="")
    notice_desc=models.CharField(max_length=300, default="")
    notice_image= models.ImageField(upload_to="clubs/images",null=True, blank=True)
    notice_date = models.DateTimeField(null=True)
    notice_document= models.FileField(upload_to="clubs/documents",null=True, blank=True)

    def __str__(self):
        return self.notice_name