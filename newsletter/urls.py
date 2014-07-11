from django.conf.urls import patterns, url

from newsletter import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/newsletter/$', views.NewsLetterView.as_view(), name='newsletter'),