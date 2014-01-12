from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'alvi.views.home', name='home'),
    url(r'^run/(?P<name>.*)$', 'alvi.views.run'),
)
