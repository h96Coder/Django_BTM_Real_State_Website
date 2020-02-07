from django.db import models
from datetime import datetime
from realtors.models import Realtor
class Listing(models.Model):
    realtors=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title =models.CharField(max_length=30)
    address=models.CharField(max_length=300)
    city =models.CharField(max_length=20)
    state =models.CharField(max_length=30)
    zipcode=models.CharField(max_length=40)
    description = models.TextField(blank=True)
    price =models.IntegerField()
    bedrooms = models.DecimalField(max_digits=4,decimal_places=2)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photo/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    photo_6 = models.ImageField(upload_to='photo/%y/%m/%d',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title


# Create your models here.
