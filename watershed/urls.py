from django.conf.urls import patterns, url
from . import views

app_name = 'watershed'

urlpatterns = [



    #GenerateGeoRSS
    url(r'^GenerateGeoRSS$', views.GenerateGeoRSS, {'type':'GenerateGeoRSS'}, name='GenerateGeoRSS'),
    url(r'^goHome$', views.index, name='index'),
    url(r'^twentymindrive_map$', views.twentymindrive_map, {'type':'twentymindrive_map'}, name='twentymindrive_map'),
    url(r'^waterlevel_map$', views.waterlevel_map, {'type': 'waterlevel_map'}, name='waterlevel_map'),

    #URL for Generic Create
    url(r'^watershed_new$', views.generic_create, {'type':'Watershed'}, name='watershed_new'),
    url(r'^florafauna_new$', views.generic_create, {'type':'floraFauna'}, name='florafauna_new'),
    url(r'^maintenance_new$', views.generic_create, {'type':'Maintenance'}, name='maintenance_new'),
    url(r'^observation_new$', views.generic_create, {'type':'Observation'},name='observation_new'),
    url(r'^ffinfo_new$', views.generic_create, {'type':'ffinfo'}, name='ffinfo_new'),
    url(r'^naturalfeature_new$', views.generic_create, {'type':'Natural Feature'},name='naturalfeature_new'),
    url(r'^manmadefeature_new$', views.generic_create,{'type':'Manmade Feature'}, name='manmadefeature_new'),
    url(r'^wpconnection_new$', views.generic_create, {'type': 'WatershedPipeConnection'}, name='wpconnection_new'),

    #URL for Generic Update
    url(r'^wpconnection/(?P<pk>.*)/update$', views.generic_update, {'type':'WatershedPipeConnection'}, name='wpconnection_update'),
    url(r'^florafauna/(?P<pk>.*)/update$', views.generic_update, {'type':'floraFauna'},name='florafauna_update'),
    url(r'^maintenance/(?P<pk>.*)/update$', views.generic_update, {'type':'Maintenance'}, name='maintenance_update'),
    url(r'^observation/(?P<pk>.*)/update$', views.generic_update,{'type':'Observation'}, name='observation_update'),
    url(r'^ffinfo/(?P<pk>.*)/update$', views.generic_update, {'type':'ffinfo'},name='ffinfo_update'),
    url(r'^naturalfeature/(?P<pk>.*)/update$', views.generic_update, {'type':'Natural Feature'}, name='naturalfeature_update'),
    url(r'^manmadefeature/(?P<pk>.*)/update$', views.generic_update, {'type':'Manmade Feature'}, name='manmadefeature_update'),
    url(r'^(?P<pk>.*)/update$', views.generic_update, {'type':'Watershed'}, name='watershed_update'),


    #URL for Generic Delete
    url(r'^wpconnection/(?P<pk>.*)/delete$', views.generic_delete, {'type': 'WatershedPipeConnection'}, name='wpconnection_delete'),
    url(r'^manmadefeature/(?P<pk>.*)/delete$', views.generic_delete, {'type':'Manmade Feature'}, name='manmadefeature_delete'),
    url(r'^naturalfeature/(?P<pk>.*)/delete$', views.generic_delete, {'type':'Natural Feature'}, name='naturalfeature_delete'),
    url(r'^ffinfo/(?P<pk>.*)/delete$', views.generic_delete, {'type':'ffinfo'}, name='ffinfo_delete'),
    url(r'^observation/(?P<pk>.*)/delete$', views.generic_delete, {'type':'Observation'}, name='observation_delete'),
    url(r'^maintenance/(?P<pk>.*)/delete$', views.generic_delete, {'type':'Maintenance'}, name='maintenance_delete'),
    url(r'^florafauna/(?P<pk>.*)/delete$', views.generic_delete, {'type':'floraFauna'}, name='florafauna_delete'),
    url(r'^(?P<pk>.*)/delete$', views.generic_delete, {'type':'Watershed'}, name='watershed_delete'),

    #URL for Generic Read
    url(r'^maintenance/(?P<pk>.*)/$', views.generic_detail, {'type':'Maintenance'},name="detail_maintenance"),
    url(r'^florafauna/(?P<pk>.*)/$', views.generic_detail, {'type':'floraFauna'}, name="detail_florafauna"),
    url(r'^observation/(?P<pk>.*)/$', views.generic_detail,{'type':'Observation'}, name='detail_observation'),
    url(r'^ffinfo/(?P<pk>.*)/$', views.generic_detail, {'type':'ffinfo'},name='detail_ffinfo'),
    url(r'^naturalfeature/(?P<pk>.*)/$', views.generic_detail, {'type':'Natural Feature'}, name='detail_naturalfeature'),
    url(r'^manmadefeature/(?P<pk>.*)/$', views.generic_detail, {'type':'Manmade Feature'}, name='detail_manmadefeature'),
    url(r'^wpconnection/(?P<pk>.*)/$', views.generic_detail, {'type': 'WatershedPipeConnection'}, name='detail_wpconnection'),




    #URL for Generic Delete


    #URL for Maintenance
    #url(r'^maintenance/(?P<pk>.*)/update$', views.maintenance_update, name='maintenance_update'),
    #url(r'^maintenance/(?P<pk>.*)/delete$', views.maintenance_delete, name='maintenance_delete'),
    #url(r'^maintenance/(?P<pk>.*)/$', views.detail_maintenance, name="detail_maintenance"),
    #url(r'^maintenance_new$', views.maintenance_create, name='maintenance_new'),



    #URL for florafauna
    #url(r'^florafauna/(?P<pk>.*)/update$', views.florafauna_update, name='florafauna_update'),
    #url(r'^florafauna/(?P<pk>.*)/delete$', views.florafauna_delete, name='florafauna_delete'),
    #url(r'^florafauna/(?P<pk>.*)/$', views.detail_florafauna, name="detail_florafauna"),
    #url(r'^florafauna_new$', views.florafauna_create, name='florafauna_new'),
    
    #URL for homepage
    url(r'^$', views.index, name="index"),

    
    #URL for Watershed
    url(r'^(?P<pk>.*)/$',views.generic_detail, {'type':'Watershed'}, name="detail"),
    # url(r'^(?P<watershed_id>[0-9]+)/$', views.detail, name="detail"),
    #url(r'^watershed_view/(?P<pk>\d+)$', views.watershed_view, name='watershed_view'),
    #url(r'^watershed_new$', views.watershed_create, name='watershed_new'),
    #url(r'^(?P<pk>.*)/update$', views.watershed_update, name='watershed_update'),
    #url(r'^(?P<pk>.*)/delete$', views.watershed_delete, name='watershed_delete'),
]
