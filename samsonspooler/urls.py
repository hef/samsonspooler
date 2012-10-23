from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'samsonspooler.views.home', name='home'),
    # url(r'^samsonspooler/', include('samsonspooler.foo.urls')),
    url('^$', redirect_to, {'url':'/thequeue/', 'permanent':False}),
    url('^thequeue/', include('thequeue.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
