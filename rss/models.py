from django.db import models
from contrib.models import CustomBaseModel
from django.utils.translation import ugettext_lazy as _


class EntryCategory(CustomBaseModel):
    """
    Categories of news (entries) from lenta.ru
    """
    name = models.CharField(_('name'), max_length=50)

    class Meta:
        verbose_name = _('entry category')
        verbose_name_plural = _('entry categories')

    def __unicode__(self):
        return self.name


class Entry(CustomBaseModel):
    """
    News (entries) from rss of lenta.ru
    """
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    published_date = models.DateTimeField(_('published date'))
    link = models.URLField(_('link'), max_length=1000)
    category = models.ForeignKey(EntryCategory, verbose_name=_('category'),
                                 related_name='entries')

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')

    def __unicode__(self):
        return self.title
