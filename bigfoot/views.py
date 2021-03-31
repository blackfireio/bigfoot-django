from django.shortcuts import render
from django.template import loader

from bigfoot.models import Sighting


def home(request):
    return render(
        request, 'index.html', {
            'sightings': Sighting.objects.all(),
        }
    )


def about(request):
    return render(request, 'about.html', {
        'foo': 'bar',
    })


def sightings_partial(request):
    return render(request, '_sightings.html', {
        'foo': 'bar',
    })


def sightings_show(request, sighting_id):
    sighting = Sighting.objects.get(id=sighting_id)
    return render(request, 'sighting_show.html', {'sighting': sighting})
