from .models import Project, UserProfile, Post, Answer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'email', 'field','text']

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('school', 'location', 'birth_date', 'job')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']