from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

class FEES(models.Model):
    fee_id = models.AutoField(primary_key=True)
    fee_sub = models.CharField(max_length=50, default="")
    fee_desc = models.CharField(max_length=500, default="")
    fee_document = models.FileField(upload_to="fee/images",null=True, blank=True)

    def __str__(self):
        return self.fee_desc



class FeeSem(models.Model):
    typee = models.CharField(max_length=5000, default="")
    pay_amount = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.typee


class FeeUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    payment_id = models.CharField(max_length=10000,default="")
    update_desc = models.CharField(max_length=5000, default="")
    amount = models.CharField(max_length=10000000,default=0)
    payment_status = models.CharField(max_length=10000000,default=0)
    transaction_id = models.CharField(max_length=10000000,default=0)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=111,default="")
    address = models.CharField(max_length=111,default="")
    roll_number = models.CharField(max_length=111,default="")
    phone = models.CharField(max_length=111, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    roll_number = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name