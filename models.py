from django.db import models

# Create your models here.

class contactinformation(models.Model):
    uname=models.CharField(max_length=20)
    unumber=models.CharField(max_length=11)
    uemail=models.CharField(max_length=20)
    umessage=models.TextField()

    def __str__(self):
        return "contact by -> "+self.uname


class admissioninfo(models.Model):
    sname=models.CharField(max_length=20)
    sfname=models.CharField(max_length=20)
    smname=models.CharField(max_length=20)
    smail=models.CharField(max_length=20)
    snumber=models.CharField(max_length=20)
    scity=models.CharField(max_length=20)
    sstate=models.CharField(max_length=20)
    sdistrict=models.CharField(max_length=20)
    sdob=models.DateField()
    saadhar=models.CharField(max_length=20)
    seducation=models.CharField(max_length=20)
    scategory=models.CharField(max_length=20)
    sgender=models.CharField(max_length=20)
    scourse=models.CharField(max_length=20)

    def __str__(self):
        return "Admission Enquiry by -> "+self.sname
    

class userregister(models.Model):
    rname=models.CharField(max_length=20)
    remail=models.CharField(max_length=20)
    rnumber=models.CharField(max_length=11)
    rpassword=models.CharField(max_length=6)

    def __str__(self):
        return self.rname



