from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime 
from datetime import date
import datetime


class Project(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    Choices=(
        ('Science','science') ,
        ('Arts ','arts'),       
        ('skills','skills'),
        )
    field=models.CharField(max_length=100 ,choices=Choices,default='all')
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='userprofiles', null=True)
    location = models.CharField(max_length=300)
    school = models.CharField(max_length=100)
    job = models.CharField(max_length=300)
    birth_date = models.DateField(null=True, blank=True)



class Post(models.Model):
    poster = models.ForeignKey(User, related_name='posts', null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
   
    created_date = models.DateTimeField(
            default=timezone.now)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    check_date=models.DateField(default=datetime.date.today)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.ForeignKey(Post, related_name='answers', null=True)
    text = models.TextField()
