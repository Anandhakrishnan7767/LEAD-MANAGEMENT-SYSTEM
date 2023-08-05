from django.contrib import admin
from.models import *

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets=[
        ('General',{'fields':['Enquiry_source']}),
        ('Phone Verification',{'fields':['Phone']}),

        ('Personal Info',{'fields':[('Student','Gender'),
        ('Email','Alternative_Email'),
        ('Address','Alternative_address'),
        ('Dob','Mobile'),
        ('Street','City'),
        ('State','District'),
        ('Pincode','Whatsapp'),
        ]}),
    ]
admin.site.register(students,StudentAdmin)