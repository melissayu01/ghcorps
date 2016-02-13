from django.conf.urls import url
from views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', populate_home_page),
    url(r'^login/$', populate_login),
    url(r'^profile/([0-9]+)$', populate_profile),
    # url(r'^forum/([0-9]+)', populate_forum),
    # url(r'^jobs/([0-9]+)', populate_jobs),
    url(r'^register/$', get_new_user),
    url(r'^thanks/$', populate_user_created),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^logout/$', populate_logout),
    url(r'^static/(.*)', return_static_file),
]
