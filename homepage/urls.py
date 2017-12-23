from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fun/$', views.fun, name='fun'),
    url(r'^projects/$', views.projects, name='projects'),
    url(
        r'^projects/instrument_design/$', views.instrument_design,
        name='instrument_design'),
    url(
        r'^projects/cluster_deposition/$', views.cluster_deposition,
        name='cluster_deposition'),
    url(
        r'^projects/molecular_beam/$', views.molecular_beam,
        name='molecular_beam'),
    url(
        r'^projects/results/$', views.results,
        name='results'),
]
