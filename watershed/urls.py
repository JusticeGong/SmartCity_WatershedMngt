from django.conf.urls import patterns, url
from . import views

app_name = 'watershed'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>.*)/$',views.detail, name="detail"),
    url(r'^(?P<pk>.*)/$',views.detail_florafauna, name="detail_florafauna"),
    # url(r'^(?P<watershed_id>[0-9]+)/$', views.detail, name="detail"),
    #url(r'^watershed_view/(?P<pk>\d+)$', views.watershed_view, name='watershed_view'),
    url(r'^watershed_new$', views.watershed_create, name='watershed_new'),
    url(r'^(?P<pk>.*)/update$', views.watershed_update, name='watershed_update'),
    url(r'^(?P<pk>.*)/delete$', views.watershed_delete, name='watershed_delete'),
    url(r'^florafauna_new$', views.florafauna_create, name='florafauna_new'),
    url(r'^(?P<pk>.*)/update$', views.florafauna_update, name='florafauna_update'),
    url(r'^(?P<pk>.*)/delete$', views.florafauna_delete, name='florafauna_delete'),
]

