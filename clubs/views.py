from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Club

from .forms import ClubForm


# Create your views here.

@login_required
def create_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.created_by = request.user # add current user
            club.save()
            return redirect('clubs:club')
    else:
        form = ClubForm()
    return render(request, 'clubs/create_club.html', {'form': form})
    
def club(request):
    try:
        club_list = get_list_or_404(Club)
    except:
        club_list = None
    
    context = {'club_list': club_list}
    return render(request, template_name="clubs/clubs.html", context=context)

def club_detail(request, id):
    club = get_object_or_404(Club, id=id)
    sessions = club.session_set.all()
    is_organiser = club.organiser.filter(id=request.user.id).exists()
    context = {
        'club': club,
        'sessions': sessions,
        'is_organiser': is_organiser,
    }
    return render(request, template_name='clubs/club_details.html', context=context)

@login_required
def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.save()
            return redirect('clubs:club')
    else:
        form = SessionForm()
    return render(request, 'clubs/create_session.html', {'form': form})

@login_required
def edit_club(request, id):
    club = get_object_or_404(Club, id=id)
    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            club = form.save(commit=False)
            club.save()
            return redirect('clubs:club_detail', id=club.id)
    else:
        form = ClubForm(instance=club)
    return render(request, 'clubs/edit_club.html', {'form': form})