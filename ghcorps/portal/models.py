from __future__ import unicode_literals

from django.db import models
import django.contrib.auth.models as authmodels
from django.contrib.auth.models import User
import datetime
import pytz

# Create your models here.

def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = os.path.join(os.getcwd(), 'portal/static/portal/images/profiles/%s.%s' % (instance.username, ext))
    return filename

def format_day(dt):
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']
    return "%s %i, %i" % (months[dt.month] ,
                          dt.day,
                          dt.year)

class UserExtra (models.Model):
    u = models.OneToOneField(User)
    fb = models.CharField(max_length = 200)
    linkedin = models.CharField(max_length = 200)
    twitter = models.CharField(max_length = 200)
    about = models.TextField()
    prof_pic = models.ImageField(upload_to=rename_file, max_length=300)

    @property
    def full_name(self):
        return ' '.join(first_name, last_name)

    def __unicode__(self):
        return "%s: %s" % (self.username, self.full_name)
    

class Job (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # nullable?
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length = 50)
    qualifications = models.TextField(max_length = 500)
    user = models.ForeignKey(User, blank = True, null = True)
    essay1 = models.TextField()
    essay2 = models.TextField()

    @property
    def date_range (self):
        return "%s -- %s" % (format_day(self.start_date),
                                  format_day(self.end_date))
    

    def __unicode__(self):
        if self.user == None:
            status = '[AVAILABLE]'
        else:
            status = '[TAKEN]'
        return "%s | %s | %s -- %s\n%s" % (self.title, 
                                            self.location, 
                                            format_day(self.start_date),
                                            format_day(self.end_date),
                                            status)

class Post (models.Model):
    subject = models.CharField(max_length = 100)
    content = models.TextField()
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return "User: %s\nDate: %s\nSubject: %s" % (self.user.username,
                                             format_day(self.dt),
                                             self.subject)
    @property
    def content_preview(self):
        preview_len = 100
        if len(self.content) > preview_len:
            return self.content[:preview_len] + "..."
        else:
            return self.content

    
    @property
    def rel_time(self):
        now = pytz.UTC.localize(datetime.datetime.now())
        dt = self.dt
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']
        diff = now - dt
        if diff < datetime.timedelta(minutes=1):
            return "%i seconds" % diff.seconds
        elif diff < datetime.timedelta(minutes=60):
            return "%i minutes" % diff.minutes
        elif diff <= datetime.timedelta(hours=23):
            return "%i hours" % int(diff.total_seconds()/3600)
        elif diff < datetime.timedelta(days=31):
            return "%i days" % diff.days
        elif now.year == dt.year:
            return "%s %i" % (months[dt.month], dt.day)
        else:
            return "%s %i, %i" % (months[dt.month], 
                                  dt.day,
                                  dt.year)

class Reply (models.Model):
    father = models.ForeignKey(Post)
    content = models.TextField()
    user = models.ForeignKey(User)
    dt = models.DateTimeField(auto_now_add = True)

    @property
    def rel_time(self):
        dt = self.dt
        now = pytz.UTC.localize(datetime.datetime.now())
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']
        diff = now - dt
        if diff < datetime.timedelta(minutes=1):
            return "%i seconds" % diff.seconds
        elif diff < datetime.timedelta(minutes=60):
            return "%i minutes" % diff.minutes
        elif diff <= datetime.timedelta(hours=23):
            return "%i hours" % int(diff.total_seconds()/3600)
        elif diff < datetime.timedelta(days=31):
            return "%i days" % diff.days
        elif now.year == dt.year:
            return "%s %i" % (months[dt.month], dt.day)
        else:
            return "%s %i, %i" % (months[dt.month], 
                                  dt.day,
                                  dt.year)
    @property
    def content_preview(self):
        preview_len = 100
        if len(content) > preview_len:
            return content[:preview_len] + "..."
        else:
            return content

    def __unicode__(self):
        return "%s's reply to %s: %s" % (self.user.username,
                                         self.father.user.username,
                                         self.content_preview)

class Activity (models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    dt = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s %s" % (self.user.username, self.text)

    @property
    def rel_time(self):
        dt = self.dt
        now = pytz.UTC.localize(datetime.datetime.now())
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']
        diff = now - dt
        if diff < datetime.timedelta(minutes=1):
            return "%i seconds" % diff.seconds
        elif diff < datetime.timedelta(minutes=60):
            return "%i minutes" % diff.minutes
        elif diff <= datetime.timedelta(hours=23):
            return "%i hours" % int(diff.total_seconds()/3600)
        elif diff < datetime.timedelta(days=31):
            return "%i days" % diff.days
        elif now.year == dt.year:
            return "%s %i" % (months[dt.month], dt.day)
        else:
            return "%s %i, %i" % (months[dt.month], 
                                  dt.day,
                                  dt.year)

class Application (models.Model):
    job = models.ForeignKey(Job)
    applicant = models.ForeignKey(User)
    essay1 = models.TextField()
    essay2 = models.TextField()
