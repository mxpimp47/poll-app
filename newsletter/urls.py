from django.conf.urls import url

from newsletter import views

urlpatterns = [
    url(r'^$', views.SignUp.as_view(), name='newsletter-signup'),
]
