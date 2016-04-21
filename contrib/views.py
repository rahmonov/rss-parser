from dateutil import parser as date_parser
from rss.models import Entry, EntryCategory


def create_entry(entry):
    """
    Creates entry object and corresponding category if they don't exist
    :param entry: one entry from rss of lenta.ru
    :return: void
    """
    category, created = EntryCategory.objects.get_or_create(
        name=entry['category'])

    Entry.objects.create(title=entry['title'],
                         description=entry['description'],
                         link=entry['link'],
                         published_date=date_parser.parse(entry['published']),
                         category=category)
