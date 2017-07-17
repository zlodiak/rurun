from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dates$', views.dates_index),
    url(r'^events$', views.events_index),
]