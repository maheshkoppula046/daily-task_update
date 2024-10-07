from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from .models import Task

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'details', 'file', 'image']