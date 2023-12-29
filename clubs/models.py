from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from locations.models import Location


# Create your models here.
class Club(models.Model):
    
    day_choices = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    
    sport_choices = [
        ('Badminton', 'Badminton'),
        ('Table Tennis', 'Table Tennis'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255, 
        default='',
        help_text='i.e. friendly/competitive, beginner/intermediate/advanced, etc.'
    )
    sport = models.CharField(choices=sport_choices, max_length=128, default='Badminton')
    day = models.CharField(
        choices=day_choices, 
        max_length=9, 
        blank=True,
        help_text="Which day of the week does your club usually play?"
        )
    time = models.TimeField(
        blank=True, 
        null=True, 
        default='20:00',
        help_text="What time does your session usually start?"
        )
    location = models.ForeignKey(
        Location, 
        on_delete=models.PROTECT,
        help_text="If you can't find your club's location, go to the Location page to add a new location first.",
        null=True,
        blank=True
        )
    price = models.IntegerField(blank=True, null=True)
    members_price = models.IntegerField(
        blank=True, 
        null=True,
        help_text="If your club has a different price for members, add this here."
        )
    rsvp_required = models.BooleanField(
        default=False, 
        help_text="Do you require RSVPs to attend your sessions?"
        )
    organiser = models.ManyToManyField(User, related_name='organiser') 
    contact = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        help_text="Contact details for enquiries and RSVP."
        )
    favourited = models.ManyToManyField(User, related_name='favourited', blank=True)
    hidden = models.BooleanField(
        default=False,
        help_text="You can turn your club into a private club by hiding it from public view."
        )
    website = models.URLField(
        blank=True, 
        null=True,
        help_text="If your club has a website, add it here."
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name