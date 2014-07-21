from django.conf.urls import url

from .views import index, post

urlpatterns = [
    url(
        regex=r'^$',
        view=index,
        name='blog-index'
    ),
    url(
        regex=r'^(?P<slug>[\w\-]+)/$',
        view=post,
        name='blog-detail'
    ),
]
