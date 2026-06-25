from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    rollno = models.IntegerField()
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    
class Mark

