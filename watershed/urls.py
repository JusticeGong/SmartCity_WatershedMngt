from django.conf.urls import url
from . import views

app_name = 'watershed'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<watershed_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^add/watershed/$', views.WatershedAdd.as_view(), name="add-watershed"),
]
