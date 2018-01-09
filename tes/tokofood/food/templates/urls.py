from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Lampung, Jakarta, Bali

urlpatternurlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                           template_name="personal/blog/blog.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,
                                                       template_name = 'personal/blog/post.html'))]
