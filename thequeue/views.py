from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from models import PrintJob, PrintJobForm
from django.template import Context, Template
from django.views.generic import TemplateView
from django.utils.timezone import now
from pprint import pprint
from django.views.generic.edit import FormView, CreateView

def current(request):
   return render(request, 'thequeue_list.html', {})

def run_job(request, key):
   printjob = PrintJob.objects.get(pk=key)
   printjob.send()
   return HttpResponse()


class PrintJobAddView(FormView):
    template_name = "thequeue_add.html"
    form_class = PrintJobForm
    success_url = "/"

    def form_valid(self, form):
        print_job = form.save(commit = False)
        print_job.submitted = now()
        print_job.save()
        return super(PrintJobAddView, self).form_valid(form)

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



