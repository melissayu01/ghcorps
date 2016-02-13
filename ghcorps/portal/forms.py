from django import forms
from django.contrib.auth.models import User

class NewUser(forms.Form):
    
    first_name = forms.CharField(label='First Name', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(label='Desired username', max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})) # make sure to later check that this is new
    email = forms.EmailField(label='Your e-mail', 
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}))
    confirm = forms.CharField(max_length=32, widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Confirm'}))
    fb = forms.CharField(max_length = 200, 
        widget = forms.TextInput(attrs={'placeholder': 'Facebook URL'}))
    twitter = forms.CharField(max_length = 200, 
        widget = forms.TextInput(attrs={'placeholder': 'Twitter URL'}))
    linkedin = forms.CharField(max_length = 200, 
        widget = forms.TextInput(attrs={'placeholder': 'LinkedIn URL'}))
    about = forms.CharField(max_length = 3000, 
        widget = forms.TextInput(attrs={'placeholder': 'Tell us a little about yourself here!'}))

    prof_pic = forms.ImageField(max_length=300)
    
    def clean_username(self):
        if len(User.objects.filter(username=self.cleaned_data.get('username', ''))) == 0:
            return self.cleaned_data.get('username', '')
        else:
            raise ValidationError("That username already exists.")
    
    def clean(self):
        if self.cleaned_data['password'] == self.cleaned_data['confirm']:
            raise ValidationError("Passwords don't match.")
        return self.cleaned_data

    def save(self):
        new_user=User.objects.create_user(self.cleaned_data['username'],
                                  self.cleaned_data['email'],
                                  self.clean_password())
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.fb = self.cleaned_data['fb']
        new_user.twitter = self.cleaned_data['twitter']
        new_user.linkedin = self.cleaned_data['linkedin']
        new_user.about = self.cleaned_data['about']
        new_user.save()

class NewPost(forms.Form):

    subject = forms.CharField(label='Subjects', max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(label='Content', max_length=4000,
        widget = forms.TextInput(attrs={'placeholder': 'Your post here.'}))

class NewReply(forms.Form):
    content = forms.CharField(label='Content', max_length=4000,
    widget = forms.TextInput(attrs={'placeholder': 'Your reply here.'}))

class NewApplication(forms.Form):
    essay1 =forms.CharField(label='Essay 1', max_length=4000,
        widget = forms.TextInput(attrs={'placeholder': 'Your response to essay 1 here.'}))
    essay2 =forms.CharField(label='Essay 2', max_length=4000,
        widget = forms.TextInput(attrs={'placeholder': 'Your response to essay 2 here.'}))

class PostJob(forms.Form):
    

