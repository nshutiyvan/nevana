from django.shortcuts import render, redirect, get_object_or_404,render_to_response
from .models import Project, UserProfile, User, Post, Answer, Friendship
from .forms import ProjectForm, UserForm, ProfileForm, PostForm, AnswerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 

#home of the project
def home(request):
    name = AnswerForm()
    return render(request,'myblog/home.html',{'name':name})

#registtation
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserForm()
    return render(request,'registration/register.html',{'form':form})

#registration of a project but which need to require login
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


#extension of userprofile
def profile(request): 
    form = ProfileForm(request.POST or None, request.FILES or None)
    user = User.objects.get(username=request.user.username)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        return redirect('new')
    else:
        form = ProfileForm()
    return render (request,"registration/register.html",{'form':form, 'user':user})



#the real template of users
def new(request):
    form = PostForm()
    all_friend = User.objects.exclude(id=request.user.id)
    name = AnswerForm()
    ok = UserProfile.objects.all()
    name = Post.objects.all().order_by('created_date').reverse()
    return render(request, 'myblog/new.html',{'form':form, 'name':name,'ok':ok,'all_friend':all_friend })

#the posted question
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    user = User.objects.get(username=request.user.username)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.poster= user
        instance.save()
        return redirect('new')
    else:
        form = PostForm()
    return render (request,"myblog/new.html",{'form':form, 'user':user})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    name = AnswerForm()
    return render(request, 'myblog/post_detail.html', {'post': post,'name':name})


def view_profile(request,pk=None):
    if pk:
        user = user.objects.get(pk=pk)
    else:
        user =request.user
    args={'user':user}
    return render(request, 'myblog/post_detail.html', args)


def answer(request):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect('new', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request,'myblog/yy.html', {'name':name})

def ok(request, pk):
    post = get_object_or_404(Answer, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.answer = post
            answer.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'myblog/n.html',{'form':form, 'post':post})

def comment(request):
    if request.method == "POST":
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save()
            return redirect('post_detail')
    else:
        form = AnswerForm()
    return render(request, 'myblog/n.html',{'form':form})

def friends_page(request, username):
  user = get_object_or_404(User, username=username)
  friends = [friendship.to_friend
             for friendship in user.friend_set.all()]
  name = user.friend_set.all()

  return render(request,'new.html', {'friends':friends, 'name':name})


