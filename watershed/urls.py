from django.conf.urls import patterns, url
from . import views

app_name = 'watershed'

urlpatterns = [

    #URL for Maintenance
    url(r'^maintenance/(?P<pk>.*)/update$', views.maintenance_update, name='maintenance_update'),
    url(r'^maintenance/(?P<pk>.*)/delete$', views.maintenance_delete, name='maintenance_delete'),
    url(r'^maintenance/(?P<pk>.*)/$', views.detail_maintenance, name="detail_maintenance"),
    url(r'^maintenance_new$', views.maintenance_create, name='maintenance_new'),



    #URL for florafauna
    url(r'^florafauna/(?P<pk>.*)/update$', views.florafauna_update, name='florafauna_update'),
    url(r'^florafauna/(?P<pk>.*)/delete$', views.florafauna_delete, name='florafauna_delete'),
    url(r'^florafauna/(?P<pk>.*)/$', views.detail_florafauna, name="detail_florafauna"),
    url(r'^florafauna_new$', views.florafauna_create, name='florafauna_new'),
    #URL for homepage
    url(r'^$', views.index, name="index"),
    #URL for Watershed
    url(r'^(?P<pk>.*)/$',views.detail, name="detail"),
    # url(r'^(?P<watershed_id>[0-9]+)/$', views.detail, name="detail"),
    #url(r'^watershed_view/(?P<pk>\d+)$', views.watershed_view, name='watershed_view'),
    url(r'^watershed_new$', views.watershed_create, name='watershed_new'),
    url(r'^(?P<pk>.*)/update$', views.watershed_update, name='watershed_update'),
    url(r'^(?P<pk>.*)/delete$', views.watershed_delete, name='watershed_delete'),
]
