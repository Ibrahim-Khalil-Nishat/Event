from django.db import models
from datetime import datetime,date
"""
# Create your models here.
class Corporate(models.Model):
    name=models.CharField(max_length=60)
    booking_details=models.TextField(max_length=300)
    date=models.IntegerField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    Email=models.EmailField()"""

class Dcorporate(models.Model):
    name=models.CharField(max_length=100)
    Details=models.CharField(max_length=200)
    date=models.DateField(auto_now_add= False,auto_now=False,blank=True,null=True)
    address=models.CharField(max_length=300)
    contact=models.CharField(max_length=15)
    Email=models.EmailField()

class Dwedding(models.Model):
    name=models.CharField(max_length=100)
    package=models.IntegerField()
    date=models.DateField(auto_now_add= False,auto_now=False,blank=True,null=True)
    address=models.CharField(max_length=300)
    contact=models.CharField(max_length=15)
    Email=models.EmailField()

class Dbirthday(models.Model):
    name=models.CharField(max_length=100)
    Details=models.CharField(max_length=200)
    date=models.DateField(auto_now_add= False,auto_now=False,blank=True,null=True)
    address=models.CharField(max_length=300)
    contact=models.CharField(max_length=15)
    Email=models.EmailField()

class specialupload(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='specialupload/')


class Review(models.Model):
    details=models.TextField()

#practice register login
class register(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=15)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)

#Admin Part

class adminregister(models.Model):
    name=models.CharField(max_length=30)
    number=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    
    
    