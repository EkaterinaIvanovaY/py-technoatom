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
        estimate = request.GET['estimate']


        if not title:
            error_title = True

        try:
            _estimate = datetime.datetime.strptime(estimate, "%Y-%m-%d")
        except:
            error_estimate = True
        #date = datetime.datetime.today()
        #delta = _estimate - date
        #days = datetime.timedelta(days = delta.days)*/
        if not (error_title or error_estimate):

            Task.objects.create(title=title, estimate=_estimate)
            return render_to_response('task.html')

    return render_to_response('task.html',
                              {'error_title': error_title, 'error_estimate': error_estimate })

def editTask(request):

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
            _estimate = datetime.date.strptime(estimate, "%Y-%m-%d")
        except:
            error_estimate = True

        if (state != "ready") or (state != "in_progress"):
            error_state = True

        if not (error_title or error_estimate or error_state):

            Task.objects.create(title=title, estimate=_estimate , state= state )
            return render_to_response('task.html')
    return render_to_response('edit_task.html',
                              {'error_title': error_title, 'error_estimate': error_estimate,'error_state': error_state,
                              })

def showTask(request):
    task_list = Task.objects.all()
    return render_to_response('show_tasks.html',
                              {"task_list": task_list})
