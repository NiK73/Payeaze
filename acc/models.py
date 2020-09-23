from django.db import models

from django.utils import timezone
from datetime import datetime  
from datetime import timedelta 

# Create your models here.

class Customer(models.Model):

    phone = models.CharField(max_length=10, default="")

    name = models.CharField(max_length=50, default="")



    def __str__(self):

        return self.phone


class Order(models.Model):
    id_no = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=50, default="")
    r_phone = models.CharField(max_length=10, default="")
    phone = models.CharField(max_length=10, default="")
    sim = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    plan = models.CharField(max_length=50, default="")
    validity = models.CharField(max_length=20, default="6")
    confirm = models.CharField(max_length=10, default="")
    price = models.IntegerField(default="0")
    t_status = models.CharField(max_length=1000, default="")
    t_token = models.CharField(max_length=1000, default="")
    date = models.DateField(default=timezone.now)
    month1 = models.BooleanField(default=False)
    month2 = models.BooleanField(default=False)
    month3 = models.BooleanField(default=False)
    month4 = models.BooleanField(default=False) 
    month5 = models.BooleanField(default=False)
    month6 = models.BooleanField(default=False)
    month7 = models.BooleanField(default=False)
    month8 = models.BooleanField(default=False)
    month9 = models.BooleanField(default=False)
    month10 = models.BooleanField(default=False)
    month11 = models.BooleanField(default=False)
    month12 = models.BooleanField(default=False)
    dmonth1 = models.DateTimeField(default=datetime.now())
    dmonth2 = models.DateTimeField(default=datetime.now()+timedelta(days=28))
    dmonth3 = models.DateTimeField(default=datetime.now()+timedelta(days=56))
    dmonth4 = models.DateTimeField(default=datetime.now()+timedelta(days=84))
    dmonth5 = models.DateTimeField(default=datetime.now()+timedelta(days=112))
    dmonth6 = models.DateTimeField(default=datetime.now()+timedelta(days=140))
    dmonth7 = models.DateTimeField(default=datetime.now()+timedelta(days=168))
    dmonth8 = models.DateTimeField(default=datetime.now()+timedelta(days=196))
    dmonth9 = models.DateTimeField(default=datetime.now()+timedelta(days=224))
    dmonth10 = models.DateTimeField(default=datetime.now()+timedelta(days=252))
    dmonth11 = models.DateTimeField(default=datetime.now()+timedelta(days=280))
    dmonth12 = models.DateTimeField(default=datetime.now()+timedelta(days=308)) 

    def __str__(self):

        return self.phone