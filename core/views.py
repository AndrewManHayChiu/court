from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from sport_sessions.models import SessionRSVP
from matches.models import Match

# @login_required
def index(request):
    current_user = request.user
    
    if current_user.is_authenticated:
        social_rsvps = SessionRSVP.objects.filter(user=current_user)
        upcoming_sessions = social_rsvps.filter(session__date__gte=timezone.now())

        matches = Match.objects.filter(
            Q(team_one__player_one=current_user.profile) | 
            Q(team_one__player_two=current_user.profile) | 
            Q(team_two__player_one=current_user.profile) | 
            Q(team_two__player_two=current_user.profile)).distinct()

        context = {
            'upcoming_sessions': upcoming_sessions,
            'matches': matches
        }
        return render(request, template_name='core/index.html', context=context)
    else:
        return render(request, template_name='core/index.html')

    
def about(request):
    return render(request, template_name='core/about.html')

def faq(request):
    return render(request, template_name='core/faq.html')

def features(request):
    return render(request, template_name='core/features.html')

def pricing(request):
    return render(request, template_name='core/pricing.html')

def privacy(request):
    return render(request, template_name='core/privacy.html')