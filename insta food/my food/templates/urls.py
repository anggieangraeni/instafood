from djangfrom django.conf.urls import url, include
from djangfrom django.views.generic import ListView, DetailView
from blog.from blog.models import Post, Bekonomi, Bsains

urlpatternurlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                           template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,
                                                       template_name = 'blog/post.html'))]
