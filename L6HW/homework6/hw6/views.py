from django.shortcuts import *
from hw6.forms import *
from hw6.models import *


def HomePage(request):
    return render(request, 'index.html', context=None)


def showTask(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    task_list = Task.objects.filter(roadmap=roadmap).order_by('state', 'estimate')
    return render(request, 'show_tasks.html', {'task_list': task_list, 'roadmap': roadmap})


def createTask(request, pk):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        task = form.save(commit=False)
        roadmap = get_object_or_404(Roadmap, pk=pk)
        task.roadmap = roadmap
        task.save()
        return redirect('/show_Roadmaps/')
    form = TaskCreateForm(None)
    return render(request, 'task.html', {'form': form})


def edit(request, pk):
    error_state = False
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if (task.state == "ready") or (task.state == "in_progress"):
                task.save()
                return redirect('/show_Roadmaps/')
            else:
                error_state = True
                return render(request, 'edit.html', {'form': form, 'error_state': error_state})
    form = TaskEditForm(instance=task)
    return render(request, 'edit.html', {'form': form, 'error_state': error_state})


def showTask(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    task_list = Task.objects.filter(roadmap=roadmap).order_by('state', 'estimate')
    return render(request, 'show_tasks.html', {'task_list': task_list, 'roadmap': roadmap})


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
    return render(request, 'roadmap.html', {'form': form})


def showRoadmaps(request):
    roadmap_list = Roadmap.objects.all()
    return render_to_response('show_Roadmaps.html',
                              {"roadmaps_list": roadmap_list})


def deleteRoadmap(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    if request.method == 'POST':
        roadmap.delete()
        return redirect('/show_Roadmaps/')
    return render(request, 'delete_roadmap.html', {'This_roadmap': roadmap})


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/show_Roadmaps/')
    return render(request, 'delete_roadmap.html', {'object': task})
