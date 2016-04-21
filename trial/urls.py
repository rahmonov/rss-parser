from django.conf.urls import url
from django.contrib import admin

from trial.views import landing

urlpatterns = [
    url(r'^$', landing, name='index'),
    url(r'^admin/', admin.site.urls),
]
