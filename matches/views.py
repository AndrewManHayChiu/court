from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MatchForm, SetForm
from .models import Match, Set

# Create your views here.
def match_list(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'matches/matches.html', context)

@login_required
def create_match_and_set(request):
    if request.method == 'POST':
        match_form = MatchForm(request.POST)
        set_form = SetForm(request.POST)
        
        if match_form.is_valid() and set_form.is_valid():
            match = match_form.save(commit=False)
            match.save()
            set = set_form.save(commit=False)
            set.match = match
            set.save()
            return redirect('matches:match')
    
    else:
        match_form = MatchForm(initial={'team_one': request.user})
        set_form = SetForm()
        
    context = {
        'match_form': match_form,
        'set_form': set_form,
    }
    
    return render(request, template_name='matches/create_match_set.html', context=context)

@login_required
def edit_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    set = get_object_or_404(Set, match=match)

    if request.method == 'POST':
        match_form = MatchForm(request.POST, instance=match)
        set_form = SetForm(request.POST, instance=set)
        if match_form.is_valid():
            match_form.save()
            set_form.save()
            return redirect('match_detail', id=match.id)
    else:
        match_form = MatchForm(instance=match)
        set_form = SetForm(instance=set)
    
    context = {
        'match_form': match_form,
        'set_form': set_form
    }
    
    return render(request, template_name='matches/edit_match.html', context=context)