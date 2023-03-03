from django.db import models

# Create your models here.


class StartUp(models.Model):
    name = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    sector = models.ForeignKey('Sector', on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='uploads/logos')
    email = models.EmailField()
    website = models.URLField(default="NA")
    date_added = models.DateTimeField(auto_now_add=True)
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='uploads/team')
    designation = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class Mentor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(default="NA")
    phone = models.CharField(max_length=20, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    current_organization = models.CharField(max_length=100, blank=True)
    current_status = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='uploads/mentors')
    area_of_interest = models.ManyToManyField('AreaOfInterest', blank=True)


class AreaOfInterest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    program = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/gallery')


class Meta(models.Model):
    vision = models.TextField()
    description = models.TextField()
    objectivies = models.ManyToManyField('Objective')
    about = models.TextField()
    our_services = models.ManyToManyField('Service')
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Objective(models.Model):
    objective = models.TextField()


class Service(models.Model):
    service = models.TextField()


class Notices(models.Model):
    update = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.update


class Invites(models.Model):
    email = models.EmailField()


class Program(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    date = models.DateField()
    image = models.ImageField(upload_to='uploads/program')
    link = models.URLField(default='NA')
