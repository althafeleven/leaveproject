from django.db import models

class Login(models.Model):
    username = models.TextField(max_length=12)
    password = models.CharField(max_length=12)
class Register(models.Model):
    firstname = models.TextField(max_length=12)
    lastname = models.TextField(max_length=12)
    adhaar = models.IntegerField
    mobile = models.IntegerField

class Leaveapply(models.Model):
    name = models.TextField(max_length=12)
    startingdate = models.TextField(max_length=12)
    endingdate = models.TextField(max_length=12)
    reason = models.TextField(max_length=12)
class Leaveapprove(models.Model):
    userid = models.TextField(default="",max_length=15,null=True)
    name = models.TextField(max_length=12)
    startingdate = models.TextField(max_length=12)
    endingdate = models.TextField(max_length=12)
    reason = models.TextField(max_length=12)
    status = models.TextField(max_length=12)
class Leavereject(models.Model):
    userid = models.TextField(default="",max_length=15,null=True)
    name = models.TextField(max_length=12)
    startingdate = models.TextField(max_length=12)
    endingdate = models.TextField(max_length=12)
    reason = models.TextField(max_length=12)
    status = models.TextField(max_length=12)

class Leavedetails(models.Model):
    userid = models.TextField(default="",max_length=15,null=True)
    name = models.TextField(max_length=12)
    startingdate = models.TextField(max_length=12)
    endingdate = models.TextField(max_length=12)
    reason = models.TextField(max_length=12)
    status = models.TextField(max_length=12)
