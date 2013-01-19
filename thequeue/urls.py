from django.conf.urls import patterns, url, include
from thequeue.views import PrintJobView, PrintJobListView, PrintJobAddView
from thequeue.views import run_job

urlpatterns = patterns (
        '',
        url(r'^new$', PrintJobAddView.as_view(), name="newprint"),
        url(r'^(?P<pk>\d+)$', PrintJobView.as_view(), name='foo'),
        url(r'^$', PrintJobListView.as_view(), name='printlist'),
)

urlpatterns += patterns(
        'thequeue.views',
        url(r'^send/(?P<key>\d+)$', 'run_job', name='run_job'),
    )
