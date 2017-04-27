import datetime
from django.shortcuts import *
from django.template import RequestContext
from django.views.generic import *
from hw5 import forms
from hw5.forms import TaskEditForm
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


def edit(request, pk):
    error_state = False

    task = get_object_or_404(Task, pk=pk)
    form = TaskEditForm(request.POST or None, instance=task)
    if form.is_valid():
        if (task.state != "ready") and (task.state != "in_progress"):
            error_state=True
        else:
           form.save()
           return redirect('/show/')
    return render(request,'edit.html',{'form':form , 'error_state': error_state})



def showTask(request):
    task_list = Task.objects.all()
    return render_to_response('show_tasks.html',
                              {"task_list": task_list})
