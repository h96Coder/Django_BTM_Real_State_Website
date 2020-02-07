from django.db import models
from datetime import datetime
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photo/%y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=300)
    email= models.CharField(max_length=57)
    is_mvp =models.BooleanField(default=True)
    hire_date =models.DateTimeField(default=False)
    hire_date =models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name

# Create your models here.
