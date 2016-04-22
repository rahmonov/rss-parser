# -*- coding: utf-8 -*-
import feedparser
try:
    import StringIO
    StringIO = StringIO.StringIO
except Exception:
    from io import StringIO
from celery import shared_task
from django.conf import settings
from contrib.views import create_entry
from rss.models import Entry
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from django.core.mail import EmailMessage


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


@shared_task
def render_to_pdf(template_src, context_dict, email):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode('utf-8')), result)

    if not pdf.err:
        message = EmailMessage('Report', 'See attached file', to=[email])
        message.attach('report.pdf', result.getvalue(), 'application/pdf')
        message.send()
        print 'report sent to email'

    print 'some error happened'  # should be logged



