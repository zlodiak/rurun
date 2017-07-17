from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('login.urls')),
    url(r'^event/', include('event.urls')),
    url(r'', include('statistic.urls')),
]
