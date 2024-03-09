from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=30,null=False)
    Email = models.EmailField(max_length=30,null=False,unique=True)
    Password = models.CharField(max_length=30,unique=True)
