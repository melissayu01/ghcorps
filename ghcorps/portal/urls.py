from django.conf.urls import url
from views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from models import *

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', populate_home_page),
    url(r'^login/$', populate_login),
    url(r'^profile/([0-9]+)$', populate_profile),
    # url(r'^forum/([0-9]+)', populate_forum),
    # url(r'^jobs/([0-9]+)', populate_jobs),
    url(r'^register/$', get_new_user),
    url(r'^thanks/$', populate_user_created),
    url(r'^logout/$', populate_logout),
    url(r'^static/(.*)', return_static_file),
]
=======
    url(r'^$', views.populate_home_page),
    url(r'^profile/([0-9]+)$', views.populate_profile),
    # url(r'^forum/([0-9]+)', views.populate_forum),
    # url(r'^jobs/([0-9]+)', views.populate_jobs),
    url(r'^register/$', views.get_new_user),
    url(r'^thanks/$', views.populate_user_created),
    url(r'^login/$', views.populate_login),
    url(r'^logout/$', views.populate_logout),
    url(r'^static/(.*)', views.return_static_file),
    url(r'^profile/$', views.temp),
]
>>>>>>> melissa
