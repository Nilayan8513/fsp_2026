from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField(default=0)
    pwd=models.CharField(max_length=50)
    phno=models.IntegerField()

    class Meta:
        db_table="user"
class student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    addrs=models.CharField(max_length=100)
    pincode=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    fathers_name=models.CharField(max_length=50)
    mothers_name=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.IntegerField()
    aadhar_no=models.IntegerField()

    class Meta:
        db_table="student"