from django.conf.urls import patterns, url, include
from thequeue.views import PrintJobView, PrintJobListView, PrintJobAddView

urlpatterns = patterns (
        '',
        url(r'^new$', PrintJobAddView.as_view(), name="newprint"),
        url(r'^(?P<pk>\d+)$', PrintJobView.as_view(), name='foo'),
        url(r'^$', PrintJobListView.as_view(), name='printlist'),
    )
