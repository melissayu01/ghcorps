from django import forms

class Registrationform(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=100)