from django import forms
from django.contrib.auth.models import User
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','contact','email','department','status','prof_pic']