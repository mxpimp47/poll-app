from django.conf.urls import url

from newsletter import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.SignUp.as_view(),
        name='newsletter-signup'
    )
]
