from django.contrib import admin
from .models import Project, UserProfile, Post,Answer

admin.site.register(Project)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Answer)