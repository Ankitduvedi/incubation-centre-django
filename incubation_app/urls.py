from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('startups', view=views.startups, name='startups'),
    path('teams', view=views.teams, name='teams'),
    path('mentors', view=views.mentors, name='mentors'),
    path('gallery', view=views.gallery, name='gallery'),
    path('invites', view=views.invites, name='invites'),
]
