from django.db import models

# Create your models here.


class Area(models.Model):
    location = models.CharField(max_length=150)
    updated= models.DateField(auto_now=True)
    
    def __str__(self):
        return self.location
    
class Escort(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    location = models.ForeignKey(Area,on_delete = models.CASCADE)
    age = models.IntegerField()
    services = models.TextField()
    orientation = models.CharField(max_length = 250)
    charges = models.IntegerField()
    country = models.CharField(max_length=250)
    email = models.EmailField()
    phoneNo = models.IntegerField()
    image = models.ImageField(upload_to='media/images', height_field=None, width_field=None, max_length=None)
    
    updated = models.DateField(auto_now =True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name
    
class Gallery(models.Model):
    escort = models.ForeignKey(Escort,on_delete= models.CASCADE)
    picture = models.ImageField(upload_to='images/gallery')
    
    