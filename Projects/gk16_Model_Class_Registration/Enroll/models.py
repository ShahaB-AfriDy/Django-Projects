from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.SmallIntegerField(primary_key=True,unique=True)
    Name = models.CharField(max_length=30)
    Reg_No = models.CharField(max_length=30,unique=True)
    Email = models.EmailField(max_length=30)

    def __str__(self):
        return self.Name

