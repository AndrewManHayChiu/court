from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    
    sports_choices = [
        ('badminton', 'Badminton'),
        ('table tennis', 'Table Tennis'),
        ('squash', 'Squash'),
        ('tennis', 'Tennis'),
        ('basketball', 'Basketball'),
        ('volleyball', 'Volleyball'),
    ]
    
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)