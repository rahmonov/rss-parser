import feedparser
from celery import shared_task
from django.conf import settings
from contrib.views import create_entry
from rss.models import Entry


@shared_task
def get_news():
    """
    Task to parse RSS of lenta.ru and save in database
    """
    lenta = feedparser.parse(settings.RSS_SOURCE)

    for entry in lenta['entries']:
        entry_exists = Entry.objects.filter(link=entry['link']).exists()

        if not entry_exists:
            create_entry(entry)

    print('done saving')



