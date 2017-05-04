"""homework5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from hw5 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^task/$', views.createTask),
    url(r'^show/(?P<pk>\d+)/$', views.showTask,name='tasks'),
    url(r'^edit/(?P<pk>\d+)/$',views.edit,name='task_edit'),
    url(r'^roadmap/$', views.create_roadmap, name='new_roadmap'),
    url(r'^show_Roadmaps/', views.showRoadmaps, name='show_roadmaps'),
    url(r'^delete_roadmap/(?P<pk>\d+)/$', views.deleteRoadmap, name='roadmap_delete'),
]

