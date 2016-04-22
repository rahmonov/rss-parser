from django.conf.urls import url, include
from django.contrib import admin

from trial.api.urls import api_urls
from trial.views import landing

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls, namespace='api')),
]

