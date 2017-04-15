from django.conf.urls import patterns, url
from . import views

app_name = 'watershed'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<watershed_id>[0-9]+)/$', views.detail, name="detail"),
    #url(r'^watershed_view/(?P<pk>\d+)$', views.watershed_view, name='watershed_view'),
    url(r'^watershed_new$', views.watershed_create, name='watershed_new'),
    url(r'^watershed_edit$', views.watershed_update, name='watershed_edit'),
    url(r'^watershed_delete$', views.watershed_delete, name='watershed_delete'),
]

