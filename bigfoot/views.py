from django.shortcuts import render
from django.template import loader
from django.db.models import Count

from bigfoot.models import Sighting


def home(request):
    return render(
        request, 'index.html', {
            'sightings': Sighting.objects.annotate(Count('comment')).all(),
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
    # prefetch_related() fixes the problem of retrieving owner for each comment
    # displayed.
    sighting = Sighting.objects.prefetch_related('comment_set__owner').get(
        id=sighting_id
    )
    return render(request, 'sighting_show.html', {'sighting': sighting})
