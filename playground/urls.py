from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'playground.views.home', name='home'),
    url(r'^run/(?P<id>\d+)$', 'playground.views.run'),

    url(r'^admin/', include(admin.site.urls)),
)
