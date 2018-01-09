from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^template/$',views.template, name='template'),
    url(r'^menu/$',views.menu, name='menu'),
    url(r'^about/$',views.about, name='about'),
    url(r'^catering/$',views.catering, name='catering'),
    url(r'^bali/$',views.bali, name='bali'),
    url(r'^jakarta/$',views.jakarta, name='jakarta'),
]
