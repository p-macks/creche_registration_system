from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    guardian = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

def __str__(self):
    return self.student_id
