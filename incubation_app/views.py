from django.shortcuts import render
from .models import StartUp, Team, Mentor, Gallery, Meta, Notices

# Create your views here.


def index(request):
    context = {}
    context['startups'] = StartUp.objects.all().order_by(
        'date_added').reverse()
    context['meta'] = Meta.objects.first()
    context['team'] = Team.objects.all()
    context['notices'] = Notices.objects.all()

    return render(request, 'incubation_app/index.html', context)


def startups(request):
    context = {}
    context['startups'] = StartUp.objects.all().order_by(
        'date_added').reverse()
    context['meta'] = Meta.objects.first()
    context['notices'] = Notices.objects.all()

    return render(request, 'incubation_app/startups.html', context)


def teams(request):
    context = {}
    context['team'] = Team.objects.all()
    context['meta'] = Meta.objects.first()
    context['notices'] = Notices.objects.all()

    return render(request, 'incubation_app/teams.html', context)


def mentors(request):
    context = {}
    context['mentors'] = Mentor.objects.all()
    context['meta'] = Meta.objects.first()
    context['notices'] = Notices.objects.all()

    return render(request, 'incubation_app/mentors.html', context)


def gallery(request):
    context = {}
    context['gallery'] = Gallery.objects.all()
    context['meta'] = Meta.objects.first()
    context['notices'] = Notices.objects.all()

    return render(request, 'incubation_app/gallery.html', context)
