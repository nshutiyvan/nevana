from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'email', 'field','text']

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    school_name = forms.CharField(max_length=300)
    class Meta:
        model = User
        fields = ('username', 'email')
