from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    city = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()

class Diploma(models.Model):
    rating = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='diplomas')
    
