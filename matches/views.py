from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render

from .forms import MatchForm, SetForm
from .models import Match

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
