import datetime
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.utils import timezone
from hw5.models import Task


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def task_form(request):
    return render_to_response('task.html')


def createTask(request):
    error_title = False
    error_estimate = False

    if 'title' in request.GET and 'estimate' in request.GET:

        title = request.GET['title']
        estimate = request.GET['estimate']

        if not title:
            error_title = True

        try:
            _estimate = datetime.datetime.strptime(estimate, "%Y-%m-%d")
        except:
            error_estimate = True

        if not (error_title or error_estimate):

            Task.objects.create(title=title, estimate=_estimate)
            return render_to_response('task.html')

    return render_to_response('task.html',
                              {'error_title': error_title, 'error_estimate': error_estimate })

def editTask(request,Task.id):

    error_title = False
    error_estimate = False
    error_state = False

    if 'title' in request.GET and 'estimate' in request.GET and 'state' in request.GET:

        title = request.GET['title']
        estimate = request.GET['estimate']
        state = request.GET['state']

        if not title:
            error_title = True
        try:
            _estimate = datetime.datetime.strptime(estimate, "%Y-%m-%d")
        except:
            error_estimate = True
        if (state != "ready") and (state != "in_progress"):
            error_state = True
        if not (error_title or error_estimate or error_state):
            new_task = Task.objects.get(id=id)
            new_task.title = title
            new_task.estimate = _estimate
            new_task.state = state
            new_task.save()
            return render_to_response('show_task.html')
    return render_to_response('edit_task.html',
                              {'error_title': error_title, 'error_estimate': error_estimate,'error_state': error_state,
                              'new_task': new_task})

def showTask(request):
    task_list = Task.objects.all()
    return render_to_response('show_tasks.html',
                              {"task_list": task_list})
