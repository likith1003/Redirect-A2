from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    pno = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    add = models.TextField()
    gender = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username