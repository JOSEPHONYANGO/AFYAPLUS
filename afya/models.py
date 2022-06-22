from django.db import models

# Create your models here.

class Doctor(models.Model):
    user_name = models.CharField(max_length=100)
