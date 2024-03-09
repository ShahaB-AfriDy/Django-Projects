from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.SmallIntegerField(primary_key=True,unique=True,null=False)
    Name = models.CharField(max_length=30)
    Reg_No = models.CharField(max_length=30,unique=True,null=False)
    Email = models.EmailField(max_length=30)
    Date = models.DateField(auto_now=False)
    Description = models.TextField(max_length=100)

