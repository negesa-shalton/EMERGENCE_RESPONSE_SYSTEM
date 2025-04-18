from django.db import models
from django.contrib.gis.db import models

from django.contrib.auth.models import User

# Create your models here.

class Incidence(models.Model):
    name = models.CharField(max_length=40,null=True)
    category = models.CharField(max_length=20, choices=[
        ('fire','Fire'),
        ('medical','Medical'),
        ('crime','Crime'),
    ], null=True)
    description = models.TextField(max_length=200,null=True)
    severity = models.CharField(max_length=20, choices=[
        ('high','High'),
        ('moderate','Moderate'),
        ('high','High'),
    ], null=True)
    
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='emergency_images/', blank=True, null=True) 
    location = models.PointField(srid=4326)
    

    class Meta:
        verbose_name_plural = 'Incidences'

    def __str__(self):
        return self.name
    

class Health_Facilities(models.Model):
    name = models.CharField(max_length=80)
    amenity = models.CharField(max_length=80)
    healthcare = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Health_Facilities'

    def __str__(self):
        return self.name