from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager

# from EMERGENCE_RESPONSE_SYSTEM import settings



# Create your models here.
############################################

class Incidence(models.Model):
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
    
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='emergency_images/', blank=True, null=True) 
    area_name = models.CharField(max_length=40,null=True)
    # location = models.PointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Incidences'

    def __str__(self):
        return self.category
    

class Health_Facilities(models.Model):
    name = models.CharField(max_length=80,null=True)
    amenity = models.CharField(max_length=80,null=True)
    healthcare = models.CharField(max_length=80,null=True)
    geom = models.MultiPointField(srid=4326,null=True)

    class Meta:
        verbose_name_plural = 'Health_Facilities'

    def __str__(self):
        return self.name if self.name else "Unnamed Facility"
    
#Creating the location model

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#Location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)  # Latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)  # Longitude
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.user.username 


#Create the user model

def get_profile_image_filepath(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return ""


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.CharField(verbose_name='date joined',auto_now_true=True)
    last_login = models.CharField(verbose_name='last joined',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,upload_to='',null=True,blank=True,default="profiles/DATABASE_CAT.jpg")
