from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from portal.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.db.models import 
from forms import *
from models import *
# from decimal import Decimal

# render home page
@login_required
def populate_home_page(request):
	if Activity.objects.exclude(user__pk = request.user.pk) <= 10:
		lst = Activity.objects.exclude(user__pk = request.user.pk).order_by('-dt')
	else:
		lst = Activity.objects.exclude(user__pk = request.user.pk).order_by('-dt')[:10]
	return render(request, 'index.html', 
		{'self_activity_list' : Activity.objects.filter(user__pk = request.user.pk),
		 'activity_list' : lst})

@login_required
def populate_jobs(request):
	return render(request, 'jobs.html', {'jobs': Job.objects.order_by('start_date')})

def temp(request):
	return render(request, 'long_profile.html')

@login_required
def populate_profile(request, user_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')

	# ensure person exists
	try:
		user = User.objects.get(username=user_id)
	except:
		raise Http404("User " + str(user_id) + " does not exist.")
		
	return render(request, 'long_profile.html', {'user': user, 
		'self_activities' : Activity.objects.filter(user__pk = user.pk),
		'self_jobs' : Job.objects.filter(user__pk = user.pk)})

# log out user
def populate_logout(request):
	logout(request)
	return render(request, 'logged_out.html', {})

# renders and handles submissions of new user
def get_new_user(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NewUser(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid() and form.cleaned_data['confirm'] == form.cleaned_data['password']:
			u = User(username = form.cleaned_data['username'],
					first_name = form.cleaned_data['first_name'],
					last_name = form.cleaned_data['last_name'],
					email = form.cleaned_data['email'],
					password = make_password(form.cleaned_data['password']))
			u.save()
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NewUser()

	return render(request, 'new_user.html', {'form': form})

# display login form and handle login requests
def populate_login(request):
	# if login request submitted, log in user if possible
	if request.method == 'POST':
		form = LogIn(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],
								password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/login/')
			else:
				return HttpResponseRedirect('/login/')
	# if login page accessed via get, display blank login form
	else:
		form = LogIn()
	
	return render(request, 'log_in.html', {'form': form})

# deals with static files (frontend)
def return_static_file(request, fname):
	try:
		f = open(os.path.join(os.getcwd(), fname))
		return HttpResponse(f.read())
	except:
		 raise Http404("File " + os.path.join(os.getcwd(), fname) + " does not exist.")

# renders registration confirmation page
def populate_user_created(request):
	return render(request, 'user_created.html', {})

# # renders review confirmation page
# def populate_review_submitted(request):
# 	return render(request, 'review_submitted.html', {})
