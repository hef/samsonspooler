from django.conf.urls import patterns, url, include
from thequeue.views import PrintJobView, PrintJobListView, PrintJobAddView

urlpatterns = patterns (
        'thequeue.views',
        url(r'^$','current'),
    )

urlpatterns += patterns (
        '',
        url(r'^new$',PrintJobAddView.as_view(), name='foo'),
        url(r'^(?P<pk>\d+)$', PrintJobView.as_view(), name='foo'),
        url(r'^list$', PrintJobListView.as_view(), name='foo'),
    )
