from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from HW5.models import Task


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def task_form(request):
    return render_to_response('task.html')


def search(request):
    if 'title' in request.GET and 'estimate' in request.GET and request.GET['title'] and request.GET['estimate']:
        title = request.GET['title']
        estimate = request.GET['estimate']
        Task.objects.create(_title = title,_estimate = estimate)

        message = 'Your title is : ' + title + "; Your estimate is : " + estimate
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
