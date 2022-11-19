from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=250)
    tg_id = models.IntegerField()
    full_name = models.CharField(max_length=250)
    location_lang = models.CharField(max_length=250)
    location_lat =models.CharField(max_length=250)
    tel = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Stores(models.Model):
    sname = models.CharField(max_length=250)
    region = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tel = models.CharField(max_length=60)
    image_url = models.CharField(max_length=250)
    location_lang = models.CharField(max_length=250)
    location_lat = models.CharField(max_length=250)
    def __str__(self):
        return "%s %s" % (self.sname, self.description)


class Products (models.Model):
    pname = models.CharField(max_length=250)
    price = models.IntegerField()
    bestbefore = models.DateTimeField() #saqlash muddati
    datamanufacture = models.DateTimeField() #ishalab chiqarilgan sana
    dataarrival = models.DateTimeField()
    count = models.IntegerField()
    types = models.CharField(max_length=20)
    qr_code = models.CharField(max_length=100 , default=None)
    discount = models.BooleanField(default=False)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)    
    def __str__(self):
        return self.pname
    
    
class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Stores, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Users, on_delete=models.CASCADE)
    production = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()
    types = models.CharField(max_length=20)
    archive = models.BooleanField(default=False)
    def __str__(self):
        return self.transactionid