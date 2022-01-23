from django.db import models
from importlib_metadata import email

# Create your models here.


#creating Database

class TeacherInformation(models.Model):
    
    name=models.CharField(max_length=200,blank=True, null=True)
    
    email=models.EmailField(blank=True, null=True)
    
    age=models.CharField(max_length=3,blank=True, null=True)
    
    phone=models.CharField(max_length=11,blank=True, null=True)
    
    department=models.CharField(max_length=11,blank=True, null=True)
    
    
    def __str__(self):
        
        return self.name   
     

class StudentInformation(models.Model):
    
    name=models.CharField(max_length=200)
    
    teacher=models.ForeignKey(TeacherInformation, related_name='students', on_delete=models.CASCADE, blank=True, null=True)
    
    email=models.EmailField()
    
    age=models.CharField(max_length=3,blank=True, null=True)
    
    phone=models.CharField(max_length=11,blank=True, null=True)
    
    department=models.CharField(max_length=11,blank=True, null=True)
    
    roll=models.CharField(max_length=11,blank=True, null=True)
    
   
    
    def __str__(self):
        
        return self.roll
    