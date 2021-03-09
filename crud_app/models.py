from django.db import models

# Create your models here.
class Student(models.Model):
    No=models.IntegerField()
    Name=models.CharField(max_length=100)
    Marks=models.IntegerField()
    Address=models.CharField(max_length=100)

