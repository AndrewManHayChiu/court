from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    
    gender_choices = [
        ('Male', 'Male'), 
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    hand_choices = [
        ('R', 'Right'),
        ('L', 'Left'),
        ('O', 'Other')
    ]
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    gender = models.CharField(choices=gender_choices, max_length=6, blank=True, editable=True)
    handedness = models.CharField(choices=hand_choices, max_length=1, blank=True, editable=True)
    follows = models.ManyToManyField(
        'self', 
        related_name='followed_by', 
        symmetrical=False, 
        blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

# Create a new profile when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()  