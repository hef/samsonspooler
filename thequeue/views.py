from django.http import HttpResponse
from django.shortcuts import render_to_response

def current(request):
    return render_to_response('thequeue_list.html', {})
