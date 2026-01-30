from django.db import models

# Create your models here.
class studentdata(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    dept = models.CharField(max_length=50)
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
        db_table="studentdata"

class contactus(models.Model):
    phno = models.IntegerField()
    email=models.EmailField()
    addr=models.TextField()

    class Meta:
        db_table="contactus"
        
class aboutus(models.Model):
    about=models.TextField()

    class Meta:
        db_table="aboutus"

class users(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField(default=0)
    pwd=models.CharField(max_length=50)
    phno=models.IntegerField()
    role=models.CharField(max_length=20,default='user')



    class Meta:
        db_table="users"
class privilage(models.Model):
    role=models.CharField(max_length=20)
    edit_aboutus=models.CharField(max_length=5, default='no')
    edit_contactus=models.CharField(max_length=5, default='no')
    edit_student_details=models.CharField(max_length=5, default='no')
    delete_students_details=models.CharField(max_length=5, default='no')
    view_student_details=models.CharField(max_length=5, default='no')
    search_students_information=models.CharField(max_length=5, default='no')
    manage_users=models.CharField(max_length=5, default='no')
    manage_privileges=models.CharField(max_length=5, default='no')

    class Meta:
        db_table="privilage"