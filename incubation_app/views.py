from django.shortcuts import render, HttpResponseRedirect
from .models import StartUp, Team, Mentor, Gallery, Meta, Notices, Invites, Program
# from .form import NewInvites

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


def invites(request):

    if request.method == "POST":
        e_mail = request.POST['email']
        print(e_mail)
        save_invite = Invites(email=e_mail)
        save_invite.save()

    return HttpResponseRedirect('/')


def programs(request):
    context = {}
    context['programs'] = Program.objects.all().order_by(
        'date').reverse()
    return render(request, 'incubation_app/programs.html', context)
