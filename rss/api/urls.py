from django.conf.urls import url
from rss.api.views import EntryList, EntryCategoryList, FilterEntry, \
    send_report

entry_urls = [
    url(r'^$', EntryList.as_view(), name='entry-list'),
    url(r'^filter/$', FilterEntry.as_view(), name='filter-entries'),
    url(r'^report/$', send_report, name='send-report'),
]

category_urls = [
    url(r'^$', EntryCategoryList.as_view(), name='category-list'),
]
