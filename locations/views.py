from django.contrib.auth.decorators import login_required
from django.core.exceptions import EmptyResultSet
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Location
from .forms import LocationForm

# Create your views here.

@login_required
def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user # add current user
            location.save()
            return redirect('locations:location')
    else:
        form = LocationForm()
    return render(request, 'locations/add_location.html', {'form': form})

def location(request):
    try:
        location_list = get_list_or_404(Location)
    except:
        location_list = None
    
    context = {'location_list': location_list}
    return render(request, template_name="locations/locations.html", context=context)

def location_detail(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    # clubs = location.social_set.all()
    context = {
        'location': location,
        # 'clubs': clubs
    }
    return render(request, template_name='locations/location_details.html', context=context)
