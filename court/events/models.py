from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    club = models.ForeignKey('clubs.Club', on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey('clubs.Location', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    player_limit = models.IntegerField()
    
    def __str__(self):
        return self.name

class EventRsvp(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    rsvp_datetime = models.DateTimeField(default=timezone.now)
    rsvp = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username + ' - ' + self.event.name