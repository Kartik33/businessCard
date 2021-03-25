from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    #birthday = forms.CharField(max_length=30)
    #age = forms.CharField(max_length=3)
    #jobtitle = forms.CharField(max_length=30)
    #employer = forms.CharField(max_length=30)
    #location = forms.CharField(max_length=30)
    #phone = forms.CharField(max_length=30)
    image = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields = (
                'username', 
                #'email', 
                'password1', 
                'password2',
                #'age',
                #'birthday',
                #'jobtitle',
                #'employer',
                #'location',
                #'phone',
                'image'
                )
