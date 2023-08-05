
from django.db import models
from django.contrib.auth.models import User
from settings.models import *

# Create your models here.
ENQUIRY_SOURCE =(
    ('youtube','YOUTUBE'),
    ('instagram','INSTAGRAM')
)
STATECHOICES = (
    ('kerala','KERALA'),
    ('karnataka','KARNATAKA'),
    ('tamilnadu','TAMILNADU'),
    ('rajasthan','RAJASTHAN')
    )
GENDER_CHOICES =(
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
)
class students(models.Model):
    Enquiry_source=models.CharField(max_length=100,choices=ENQUIRY_SOURCE,default='youtube')
    Phone=models.CharField(max_length=20,null=True)
    Student=models.CharField(max_length=20,null=True)
    Email=models.EmailField(max_length=20,null=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Dob=models.DateField(null=True)
    Street=models.CharField(max_length=20,null=True,blank=True)
    State=models.CharField(max_length=20,choices=STATECHOICES)
    Pincode=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    Alternative_Email=models.EmailField(max_length=20,null=True,blank=True)
    Alternative_address=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.CharField(max_length=20,null=True,blank=True)
    City=models.CharField(max_length=20,null=True,blank=True)
    District=models.CharField(max_length=20)
    Whatsapp=models.CharField(max_length=20,null=True)


   









    class Meta:
        verbose_name_plural='students'