from django.contrib import admin
from .models import Project, UserProfile, Post,Answer,Friendship,FriendMgmt

admin.site.register(Project)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Friendship)
admin.site.register(FriendMgmt)