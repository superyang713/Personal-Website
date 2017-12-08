from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from sammy_blog.models import Post
app_name = 'sammy_blog'

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="sammy_blog/index.html"), name='index'),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post, template_name="sammy_blog/detail.html")),
]