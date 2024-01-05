import uuid 

from datetime import datetime
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


from members.models import Profile
from sport_sessions.models import Session

# Create your models here.
class Team(models.Model):
    player_one = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='teams_as_player_one')
    player_two = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='teams_as_player_two', blank=True, null=True) 
    
    def save(self, *args, **kwargs):
        # Check if a team with the same players already exists
        if self.pk is None: # Only do this for new records
            try:                
                if self.player_two:
                    return Team.objects.get(
                        Q(player_one=self.player_one, player_two=self.player_two) |
                        Q(player_one=self.player_two, player_two=self.player_one)
                    )
                else:
                    return Team.objects.get(player_one=self.player_one, player_two=None)
            except Team.DoesNotExist:
                pass
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.player_two:
            return f"{self.player_one} and {self.player_two}"
        
        else:
            return f"{self.player_one}"

class Match(models.Model):
    
    sport_choice = [
        ('badminton', 'Badminton'),
        # ('table_tennis', 'Table Tennis'),
    ]
    
    combination_type_choice = [
        ('MS', 'Mens Singles'),
        ('WS', 'Womens Singles'),
        ('MD', 'Mens Doubles'),
        ('WD', 'Womens Doubles'),
        ('XD', 'Mixed Doubles'),
    ]
        
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now, null=False, blank=False, editable=True)
    time = models.TimeField(default=timezone.now, blank=True, editable=True)
    
    is_doubles = models.BooleanField(default=True)
    combination = models.CharField(choices=combination_type_choice, default='MD', max_length=2)
    
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_as_team_two', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
    
    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super().save(*args, **kwargs)

class Set(models.Model):
    
    team_choice = [
        ('team1', 'Team 1'),
        ('team2', 'Team 2'),
    ]
    
    set_choice = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    
    match = models.ForeignKey(Match, related_name='sets', on_delete=models.CASCADE)
    set = models.IntegerField(choices=set_choice, default=1)
    winning_team = models.CharField(choices=team_choice, max_length=5)
    team_one_score = models.IntegerField(default=21)
    team_two_score = models.IntegerField()
    
    class Meta:
        verbose_name = 'Set'
        verbose_name_plural = 'Sets'
    
    def __str__(self):
        return f"Match: {self.match} - Set: {self.set} - Winner: {self.winning_team}"
    
    def clean(self):
        # Call the base implementation first to get a full clean.
        super().clean()
        

class Rally(models.Model):
    
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True)
    rally_number = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Rally'
        verbose_name_plural = 'Rallies'

    def __str__(self):
        return f"Rally {self.rally_number}"