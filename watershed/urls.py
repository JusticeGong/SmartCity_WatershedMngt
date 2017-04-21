from django.conf.urls import patterns, url
from . import views

app_name = 'watershed'

urlpatterns = [
    # URL for Observation
    url(r'^observation/(?P<pk>.*)/update$', views.observation_update, name='observation_update'),
    url(r'^observation/(?P<pk>.*)/delete$', views.observation_delete, name='observation_delete'),
    url(r'^observation/(?P<pk>.*)/$', views.detail_observation, name="detail_observation"),
    url(r'^observation_new$', views.observation_create, name='observation_new'),

    # URL for ffInfo
    url(r'^ffinfo/(?P<pk>.*)/update$', views.ffinfo_update, name='ffinfo_update'),
    url(r'^ffinfo/(?P<pk>.*)/delete$', views.ffinfo_delete, name='ffinfo_delete'),
    url(r'^ffinfo/(?P<pk>.*)/$', views.detail_ffinfo, name="detail_ffinfo"),
    url(r'^ffinfo_new$', views.ffinfo_create, name='ffinfo_new'),

    # URL for NaturalFeature
    url(r'^naturalfeature/(?P<pk>.*)/update$', views.naturalfeature_update, name='naturalfeature_update'),
    url(r'^naturalfeature/(?P<pk>.*)/delete$', views.naturalfeature_delete, name='naturalfeature_delete'),
    url(r'^naturalfeature/(?P<pk>.*)/$', views.detail_naturalfeature, name="detail_naturalfeature"),
    url(r'^naturalfeature_new$', views.naturalfeature_create, name='naturalfeature_new'),

    # URL for ManmadeFeature
    url(r'^manmadefeature/(?P<pk>.*)/update$', views.manmadefeature_update, name='manmadefeature_update'),
    url(r'^manmadefeature/(?P<pk>.*)/delete$', views.manmadefeature_delete, name='manmadefeature_delete'),
    url(r'^manmadefeature/(?P<pk>.*)/$', views.detail_manmadefeature, name="detail_manmadefeature"),
    url(r'^manmadefeature_new$', views.manmadefeature_create, name='manmadefeature_new'),

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
