from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.days_spa, name='days_spa'),
    url(r'^days$', views.days_index, name='days_index'),
    url(r'^days/(?P<timestamp_begin>[0-9]+)/(?P<timestamp_end>[0-9]+)$', views.days_read, name='days_read'),
]