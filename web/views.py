from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm, UserForm


def home(request):
	 name = SchoolForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request,'myblog/home.html',{'form':form,'name':name })

def project(request):
    name = Project.objects.all()
    science=Project.objects.filter(field='science').order_by('created_date').reverse()
    arts=Project.objects.filter(field='science').order_by('created_date').reverse()
    skills=Project.objects.filter(field='science').order_by('created_date').reverse()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save()
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'myblog/project.html', {'form': form, 'name':name,'name':name, 'science':science,'arts':arts,'skills':skills})
