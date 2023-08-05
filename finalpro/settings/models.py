from django.db import models

# Create your models here.

class company(models.Model):
    company=models.CharField(max_length=100,null=True)
    adress1=models.CharField(max_length=100,null=True,blank=True)
    adress2=models.CharField(max_length=100,null=True,blank=True)
    adress3=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    website=models.CharField(max_length=100,null=True,blank=True)
    logo=models.ImageField(null=True)
    active=models.BooleanField(default=True)

    class Meta:
         verbose_name_plural='companies'

    
    def __str__(self):
        return self.company
   

class state(models.Model):
    statename=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)


    class Meta:
         verbose_name_plural='states'

    def __str__(self):
        return self.statename
    
STATE_CHOICES = (
    ('kerala','KERALA'),
    ('karnataka','KARNATAKA'),
    ('tamilnadu','TAMILNADU'),
    ('rajasthan','RAJASTHAN')
)

class district(models.Model):
    state=models.CharField(max_length=100,null=True,choices=STATE_CHOICES)
    district_name=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)


#     class Meta:
#          verbose_name_plural='districts'

    def __str__(self):
        return self.state
    
# DISTRICT_CHOICES = (
#     ('kasargod','KASARGOD'),
#     ('kannur','KANNUR'),
#     ('kozhikkode','KOZHKKODE'),
#     ('wayanad','WAYANAD'),
#     ('malappuram','MLAPPURAM'),
#     ('palakkad','PALAKKAD')
# )    




class branch(models.Model):
    branch=models.CharField(max_length=100,null=True)
    branchcode= models.CharField(max_length=100,null=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    street=models.CharField(max_length=100,null=True,blank=True)
    
    state=models.ForeignKey(state,on_delete=models.CASCADE,null=True)
    district=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    
    pincode=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    active=models.BooleanField(default=True)

    class Meta:
         verbose_name_plural='branches'

    def __str__(self):
        return self.branch
     



class enquirey_source(models.Model):
   enquireysoursename= models.CharField(max_length=100,null=True)
   active=models.BooleanField(default=True)

   class Meta:
         verbose_name_plural='enquiry sources'
         verbose_name='enquiry sources'

   def __str__(self):
        return self.enquireysoursename


   


class follow_up_status(models.Model):
    followupstatusname=models.CharField(max_length=100,null=True)
    followupstatus=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)

    class Meta:
         verbose_name_plural='follow up statuses'
         verbose_name='follow up status'

    def __str__(self):
        return self.followupstatus



class qualification(models.Model):
    qualification=models.CharField(max_length=100,null=True)
    active=models.BooleanField(default=True)

    class Meta:
         verbose_name_plural='qualifications'

    def __str__(self):
        return self.qualification
     
    


class batch(models.Model):
        course=models.CharField(max_length=100,null=True)   
        trainer=models.CharField(max_length=100,null=True) 
        start_date=models.DateField(max_length=100,null=True) 
        end_date=models.DateField(max_length=100,null=True)
        closed=models.BooleanField()
        active=models.BooleanField(default=True) 

        class Meta:
         verbose_name_plural='batches'

        def __str__(self):
             return self.course
 


class master_data(models.Model):
        name=models.CharField(max_length=100,null=True) 
        value=models.CharField(max_length=100,null=True) 
        type=models.CharField(max_length=100,null=True) 
        active=models.BooleanField(default=True)

        class Meta:
         verbose_name_plural='master data'
         verbose_name='master data'

        def __str__(self):
          return self.name









 


     

        
