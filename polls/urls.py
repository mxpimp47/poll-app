from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='polls-index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='polls-detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='polls-results'),
]
