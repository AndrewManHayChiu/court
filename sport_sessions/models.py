import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from clubs.models import Club

# Create your models here.
class Session(models.Model):
    # Add uuid as public identifier
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    date = models.DateField()
    start_time = models.TimeField(default='20:00')
    end_time = models.TimeField(default='22:00')
    doubles = models.BooleanField(default=True)
    singles = models.BooleanField(default=False)
    max_attendees = models.PositiveIntegerField(default=30, blank=True, null=True)
    waiting_list_enabled = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    hidden = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.club}, {self.date}, {self.start_time}"
    
    def is_full(self):
        if self.max_attendees and self.rsvps.count() >= self.max_attendees:
            return True
        else:
            return False

class SessionRSVP(models.Model):
    
    payment_method_choices = [
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),
        ('other', 'Other'),
    ]
    
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=10, choices=payment_method_choices)
    
    # Allow admins to add non-users to the RSVP list
    non_user_name = models.CharField(max_length=255, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('session', 'user') # Prevents duplicates (can't rsvp more than once)
        
    def __str__(self):
        if self.non_user_name:
            return f"{self.non_user_name} - {self.session} - Attending: {self.is_attending}"
        else:
            return f"{self.user} - {self.session} - Attending: {self.is_attending}"
    
    def save(self, *args, **kwargs):
        if self.session.max_attendees and self.session.rsvps.count() >= self.session.max_attendees:
            raise ValidationError('Sorry, this session is full.')
        super().save(*args, **kwargs)

