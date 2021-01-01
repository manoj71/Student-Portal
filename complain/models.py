from django.db import models

class Contactcomplain(models.Model):
    contact_id  = models.AutoField(primary_key=True)
    query_status = models.CharField(max_length=5000, default="Pending")
    querytype = models.CharField(max_length=5000, default="")
    querydesc = models.CharField(max_length=5000, default="")
    querysub = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=111,default="")
    phone = models.CharField(max_length=111,default="")
    rollnumber = models.CharField(max_length=111,default="")
    branchyear = models.CharField(max_length=111, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.query_status + "----" + self.querysub + "---" + self.rollnumber


class Contactenquiry(models.Model):
    contact_id  = models.AutoField(primary_key=True)
    query_status = models.CharField(max_length=5000, default="")
    querytype = models.CharField(max_length=5000, default="")
    querydesc = models.CharField(max_length=5000, default="")
    querysub = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=111,default="")
    phone = models.CharField(max_length=111,default="")
    rollnumber = models.CharField(max_length=111,default="")
    branchyear = models.CharField(max_length=111, default="")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.query_status + "----" + self.querysub + "---" + self.rollnumber
