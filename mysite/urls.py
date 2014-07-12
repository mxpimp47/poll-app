from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls))
]
