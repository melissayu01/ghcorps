from __future__ import unicode_literals

from django.db import models
import django.contrib.auth.models as authmodels

# Create your models here.

def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = os.path.join(os.getcwd(), 'portal/static/portal/images/profiles/%s.%s' % (instance.username, ext))
    return filename

class User (authmodels.User):
    fb = models.CharField(max_length = 200)
    linkedin = models.CharField(max_length = 200)
    twitter = models.CharField(max_length = 200)
    about = models.TextField()
    prof_pic = models.ImageField(upload_to=rename_file, max_length=300)

class Job (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField() # nullable?
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length = 50)
    qualifications = models.TextField(max_length = 500)
    user = models.ForeignKey(user)
    essay1 = models.TextField()
    essay2 = models.TextField()

class Post (models.Model):
    subject = models.CharField(max_length = 100)
    content = models.TextField()
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add = True)

class Reply (models.Model):
    father = models.ForeignKey(Post)
    content = models.TextField()
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add = True)

class Activity = (models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    dt = models.DateTimeField(auto_now_add = True)

class Application (models.Model):
    job = models.ForeignKey(Job)
    applicant = models.ForeignKey(User)
    essay1 = models.TextField()
    essay2 = models.TextField()
