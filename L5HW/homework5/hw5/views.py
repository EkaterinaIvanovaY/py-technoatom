from datetime import datetime

from django.shortcuts import *
from hw5.forms import *
from hw5.models import Task


def HomePage(request):
    return render(request, 'index.html')


def createTask(request):
    estimate = request.POST.get('estimate')
    if estimate is not None:
        try:
            datetime.strptime(estimate, "%Y-%m-%d")
            form = TaskCreateForm(request.POST)
            form.save()
            return redirect('/show/')
        except:
            error_estimate = True
            form = TaskCreateForm(None)
            return render(request, 'task.html',
                          {'form': form, 'error_title': error_title, 'error_estimate': error_estimate})

    form = TaskCreateForm(None)
    return render(request, 'task.html', {'form': form } )

def editTask(request, pk):
    error_title = False
    error_estimate = False
    error_state = False

    task = get_object_or_404(Task, pk=pk)
    # В этом месте происходит обработка request.POST
    # здесь же обнаржуиваются ошибки
    # первое что приходит в голову - поступить как колхозник
    estimate = request.POST.get('estimate')
    if estimate is not None:
        try:
            datetime.strptime(estimate, "%Y-%m-%d")
            form = TaskEditForm(request.POST, instance=task)
            if form.is_valid():
                if (task.state == "ready") or (task.state == "in_progress"):
                    form.save()
                    return redirect('/show/')
                else:
                    error_state = True
            return render(request, 'edit.html',
                          {'form': form, 'error_title': error_title, 'error_estimate': error_estimate,
                           'error_state': error_state})
        except:
            error_estimate = True
            form = TaskEditForm(instance=task)
            return render(request, 'edit.html',
                      {'form': form, 'error_title': error_title, 'error_estimate': error_estimate, 'error_state': error_state})

    form = TaskEditForm(instance=task)
    return render(request, 'edit.html',
                  {'form': form, 'error_title': error_title, 'error_estimate': error_estimate,
                   'error_state': error_state})


def showTask(request):
    task_list = Task.objects.all()
    return render(request, 'show_tasks.html',
                              {"task_list": task_list})
