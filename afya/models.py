from django.db import models
from . import forms

# Create your models here.
class Doctor(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=255, blank=True)
    contact = models.CharField(max_length=20,null=True)
    prof_pic= models.ImageField(upload_to='prof_pic/',null=True,blank=True)
    department= models.CharField(max_length=50,choices=departments,default='Pediatrician')
    address = models.CharField(max_length=40)
    status=models.BooleanField(default=False)

    def __str__(self):
        self.username = self.username

