from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^project$', views.project, name='project'),
    url(r'^new$', views.new, name='new'),
    url(r'^register$', views.register, name='register'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^answer/(?P<pk>\d+)/$', views.answer, name='answer'),
    url(r'^post_create$', views.post_create, name='post_create'),
    url(r'^post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^ok/(?P<pk>\d+)/$', views.ok, name='ok'),
    url(r'^comment$', views.comment, name='comment'),
    url(r'^friend/(?P<username>\d+)/$', views.friends_page, name='friends_page'),
    url(r'^accounts/(?P<pk>\d+)/$', views.view_profile, name='view_profile'),
    ]