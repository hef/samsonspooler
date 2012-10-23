from django.conf.urls import patterns, url, include

urlpatterns = patterns(
        'thequeue.views',
        (r'^$','current'),
        )
