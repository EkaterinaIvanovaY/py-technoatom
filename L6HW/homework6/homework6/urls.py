from django.conf.urls import url, include
from hw6 import views

urlpatterns = [
    url(r'^$', views.HomePage, name='home' ),
    url(r'^show/(?P<pk>\d+)/new_task/$', views.createTask, name='new_task'),
    url(r'^show/(?P<pk>\d+)/$', views.showTask,name='tasks'),
    url(r'^show/(?P<pk>\d+)/edit/$',views.edit,name='task_edit'),
    url(r'^show/(?P<pk>\d+)/delete_task/$',views.deleteTask,name='task_delete'),
    url(r'^roadmap/$', views.create_roadmap, name='new_roadmap'),
    url(r'^show_Roadmaps/', views.showRoadmaps, name='show_roadmaps'),
    url(r'^delete_roadmap/(?P<pk>\d+)/$', views.deleteRoadmap, name='roadmap_delete'),
]

