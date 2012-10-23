from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from models import PrintJob, PrintJobForm
from django.template import Context, Template

def current(request):
   return render(request, 'thequeue_list.html', {})

def add_job(request):
    context = Context()
    if request.method == 'POST':
        form = PrintJobForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        context['form'] = PrintJobForm()
    return render(request, 'thequeue_add.html', context)


