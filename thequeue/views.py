from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from models import PrintJob, PrintJobForm
from django.template import Context, Template
from django.views.generic import TemplateView
from django.utils.timezone import now
def current(request):
   return render(request, 'thequeue_list.html', {})


class PrintJobAddView(TemplateView):
    template_name = "thequeue_add.html"

    def get_context_data(self, **kwargs):
        context = super(PrintJobAddView, self).get_context_data(**kwargs)
        #context['printjob'] = PrintJob.find(pk=1)
        context['form'] = PrintJobForm()
        return context

    def post(self, request, *args, **kwargs):
        form = PrintJobForm(request.POST)
        if form.is_valid():
            pj = PrintJob()
            pj.title = form.cleaned_data['title']
            pj.submitted = now()
            pj.save()
            return HttpResponseRedirect('/')
        return HttpResponse('nope')

class PrintJobView(TemplateView):
    template_name = "thequeue_printjob.html"

    def get_context_data(self, **kwargs):
        context = super(PrintJobView, self).get_context_data(**kwargs)
        return context

class PrintJobListView(TemplateView):
    template_name = "thequeue_printjoblist.html"

    def get_context_data(self, **kwargs):
        context = super(PrintJobListView, self).get_context_data(**kwargs)
        context['jobs'] = PrintJob.objects.all()
        return context;
