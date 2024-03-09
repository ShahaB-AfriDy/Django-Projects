from django.db import models

# Create your models here.
class Login_Model(models.Model):
    User = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)