from django.conf.urls import url, include, patterns

from rss.api.urls import entry_urls, category_urls
from trial.api import views

api_urls = patterns(
    '',
    url(r'^$', views.api_root),
    url(r'^entries/', include(entry_urls, namespace='entries')),
    url(r'^categories/', include(category_urls, namespace='categories')),
)
