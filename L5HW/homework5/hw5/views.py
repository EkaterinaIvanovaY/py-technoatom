from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from hw5.models import Task


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def task_form(request):
    return render_to_response('task.html')


def search(request):
    error = False
    if 'title' in request.GET and 'estimate' in request.GET:
        title = request.GET['title']
        estimate = request.GET['estimate']
        if not (title and estimate):
            error = True
        else:
            Task.objects.create(title=title, estimate=estimate)
            task_list = Task.objects.all()
            return render_to_response('show_tasks.html',
                                                    {'task_list': task_list, 'title': title})
    return render_to_response('task.html',
                                    {'error': error})


def show(request):
    task_list = Task.objects.all()
    return render_to_response('show_tasks.html',
                                            {"task_list": task_list} )