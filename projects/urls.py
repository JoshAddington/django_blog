from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        url(r'^$', views.project_list),
        url(r'^(?P<pk>[0-9]+)/$', views.project_detail),
        url(r'^new/$', views.project_new, name='project_new'),
        url(r'^(?P<pk>[0-9]+)/edit/$', views.project_edit, name='project_edit'),
        url(r'^(?P<pk>[0-9]+)/publish/$', views.project_publish, name='project_publish'),
        url(r'^(?P<pk>[0-9]+)/delete/$', views.project_delete, name='project_delete'),
        url(r'^drafts/$', views.project_draft_list, name='project_draft_list'),
)
