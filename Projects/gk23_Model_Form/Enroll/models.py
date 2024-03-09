from django.db import models

# Create your models here.

class Student(models.Model):
    Id = models.PositiveSmallIntegerField(primary_key=True,unique=True,)
    Name = models.CharField(max_length=30)
    Reg_No = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=30)