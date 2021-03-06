from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import lampung

urlpatterns = [url(r'^$', ListView.as_view(queryset=lampung.objects.all().order_by("-date")[:25],
                                           template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=lampung,
                                                       template_name = 'blog/post.html'))]
