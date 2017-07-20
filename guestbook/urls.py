from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.messages_spa),
    url(r'^message_create$', views.message_create),
]