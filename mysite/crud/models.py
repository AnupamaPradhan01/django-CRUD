from django.db import models

class Student(models.Model):
    stuid=models.CharField(max_length=70)
    stuname=models.CharField(max_length=110)
    stuemail=models.CharField(max_length=110)
    stupass=models.CharField(max_length=110)
