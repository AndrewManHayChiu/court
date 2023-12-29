import uuid 

from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from members.models import Profile
from sport_sessions.models import Session

# Create your models here.
class Team(models.Model):
    
    players = models.ManyToManyField(Profile, blank=True) # Blank so matches can be recorded even without knowing the opponent
    team_name = models.TextField(blank=True) # Optional team name
    
    def __str__(self):
        return self.team_name

class Match(models.Model):
    
    sport_choice = [
        ('badminton', 'Badminton'),
        ('table_tennis', 'Table Tennis'),
    ]
    
    team_choice = [
        ('team1', 'Team 1'),
        ('team2', 'Team 2'),
    ]
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now, null=False, blank=False, editable=True)
    time = models.TimeField(default=timezone.now, blank=True, editable=True)
    
    is_doubles = models.BooleanField(default=True)
    
    team_one = models.ManyToManyField(User, related_name='team_one')
    team_two = models.ManyToManyField(User, related_name='team_two', blank=True)
    
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
    winner_score = models.IntegerField(default=21)
    loser_score = models.IntegerField()
    
    class Meta:
        verbose_name = 'Set'
        verbose_name_plural = 'Sets'
    
    def __str__(self):
        return f"Match: {self.match} - Set: {self.set} - Winner: {self.winning_team}"

class Rally(models.Model):
    
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True)
    rally_number = models.IntegerField()
    server = models.ForeignKey(User, on_delete=models.PROTECT, related_name='server')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='receiver')
    shot = models.CharField(max_length=20)
    rally_result = models.CharField(max_length=20, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Rally'
        verbose_name_plural = 'Rallies'

    def __str__(self):
        return f"Rally {self.rally_number}"