from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Reg_NO = models.CharField(max_length=30,unique=True)
    Email = models.EmailField(max_length=30)
