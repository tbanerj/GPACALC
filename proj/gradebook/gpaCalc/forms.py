from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ClassForm(forms.Form):
    name = forms.CharField(label="Class Name")
    letterGrade = forms.CharField(label="Grade", max_length=1)
    credits = forms.IntegerField(label="Credits")
