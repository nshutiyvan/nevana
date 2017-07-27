from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^project$', views.project, name='project'),
    url(r'^new$', views.new, name='new'),
    url(r'^register$', views.register, name='register'),
    ]