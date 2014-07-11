from django.conf.urls import url

from newsletter import views

urlpatterns = [
	url(r'^(?P<pk>\d+)/newsletter/$', views.NewsLetterView.as_view(), name='newsletter'),
]