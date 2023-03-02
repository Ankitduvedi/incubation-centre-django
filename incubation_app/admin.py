from django.contrib import admin
from .models import AreaOfInterest, Sector, Stage, StartUp, Team, Mentor, Gallery, Meta, Service, Objective, Notices, Invites

# Register your models here.
admin.site.register(StartUp)
admin.site.register(Team)
admin.site.register(Mentor)
admin.site.register(AreaOfInterest)
admin.site.register(Sector)
admin.site.register(Stage)
admin.site.register(Gallery)
admin.site.register(Meta)
admin.site.register(Service)
admin.site.register(Objective)
admin.site.register(Notices)
admin.site.register(Invites)
