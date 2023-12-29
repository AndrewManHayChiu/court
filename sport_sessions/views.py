from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from clubs.models import Club
from .models import Session, SessionRSVP
from .forms import SessionForm, EditSessionForm

def session(request):
    now = timezone.now()
    upcoming_sessions = Session.objects.filter(date__gte=now).order_by('date')
    past_sessions = Session.objects.filter(date__lt=now).order_by('-date')
    return render(
        request, 
        template_name='sport_sessions/sessions.html', 
        context={
            'upcoming_sessions': upcoming_sessions,
            'past_sessions': past_sessions,
            })

def session_detail(request, uuid):
    session = get_object_or_404(Session, uuid=uuid)
    club = session.club
    attendees = session.rsvps.all()
    is_organiser = club.organiser.filter(id=request.user.id).exists()
    context = {
        'session': session,
        'club': club,
        'attendees': attendees,
        'is_organiser': is_organiser,
    }
    return render(
        request, 
        template_name='sport_sessions/session_details.html', 
        context=context)

@login_required
def create_session(request):
    club_id = request.GET.get('club_id')
    club = Club.objects.get(id=club_id)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.club = club
            session.save()
            return redirect('clubs:club_detail', id=club_id)
    else:
        form = SessionForm()
    return render(
        request, 
        template_name='sport_sessions/create_session.html', 
        context={'form': form})
    
@login_required
def edit_session(request, id):
    session = get_object_or_404(Session, id=id)
    club = session.club
    if request.method == 'POST':
        form = EditSessionForm(request.POST, instance=session)
        if form.is_valid():
            session = form.save(commit=False)
            session.save()
            return redirect('clubs:club_detail', id=club.id)
    else:
        form = EditSessionForm(instance=session)
    
    return render(
        request, 
        template_name='sport_sessions/edit_session.html', 
        context={'form': form, 'session': session})
    
class SessionRSVPCreateView(generic.View):
    
    def post(self, request, *args, **kwargs):
        session = get_object_or_404(Session, id=self.kwargs['id'])
        
        if session.max_attendees and session.rsvps.count() >= session.max_attendees:
            # raise ValidationError('Sorry, this session is full.')
            return render(request, 'sport_sessions/session_full.html')
        
        
        SessionRSVP.objects.create(session=session, user=request.user, is_attending=True)
        
        return redirect('sport_sessions:session_detail', id=session.id)