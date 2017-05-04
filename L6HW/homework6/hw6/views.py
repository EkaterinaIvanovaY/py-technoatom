import datetime
from django.shortcuts import *
from django.template import RequestContext
from django.views.generic import *
from hw6 import forms
from hw6.forms import *
from hw6.models import *



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def task_form(request):
    return render_to_response('task.html')


def createTask(request):
    title = request.POST.get('title')
    estimate = request.POST.get('estimate')
    if estimate is not None:
        error_title = False
        if title is None:
            error_title = True
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

def edit(request, pk):
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



def showTask(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    task_list = Task.objects.filter(roadmap=roadmap).order_by('state', 'estimate')
    return render(request, 'show_tasks.html', {'task_list': task_list})


def create_roadmap(request):
    if request.method == "POST":
        form = RoadmapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show_Roadmaps/')
        else:
            pass
    else:
        form = RoadmapForm()
    return render(request,'roadmap.html',{'form':form})

def showRoadmaps(request):
    roadmap_list = Roadmap.objects.all()
    return render_to_response('show_Roadmaps.html',
                              {"roadmaps_list": roadmap_list})

def deleteRoadmap(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    if request.method == 'POST':
      roadmap.delete()
      return redirect('/show_Roadmaps/')
    return render(request, 'delete_roadmap.html',{'This_roadmap':roadmap})