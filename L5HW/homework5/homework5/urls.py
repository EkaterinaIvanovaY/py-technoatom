
from django.conf.urls import url, include

from hw5 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^task/', views.task_form),
    url(r'^search/', views.search),
    url(r'^show/', views.show)
]
