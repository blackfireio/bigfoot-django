from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Count

from bigfoot.models import Sighting


def home(request):
    return render(
        request, 'index.html', {
            'sightings': Sighting.objects.annotate(Count('comment')).all()[:25],
        }
    )


def about(request):
    return render(request, 'about.html', {
        'foo': 'bar',
    })


def sightings_partial(request):
    requested_page = int(request.GET.get('page', 1))

    max = 25
    limit = max * requested_page
    offset = (requested_page - 1) * max
    sightings = Sighting.objects.all()[offset:limit]

    html = loader.render_to_string(
        '_sightings.html', {'sightings': sightings}, request
    )
    next = requested_page + 1

    return JsonResponse({
        'html': html,
        'next': next,
    })


def sightings_show(request, sighting_id):
    # prefetch_related() fixes the problem of retrieving owner for each comment
    # displayed.
    sighting = Sighting.objects.prefetch_related('comment_set__owner').get(
        id=sighting_id
    )
    return render(request, 'sighting_show.html', {'sighting': sighting})
