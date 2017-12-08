from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fun/$', views.fun, name='fun'),
    url(r'^projects/$', views.projects, name='projects'),
]
