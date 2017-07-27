from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=300)
    school = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    birth_date = models.DateField(null=True, blank=True)


 