from django.contrib import admin
from rss.models import EntryCategory, Entry


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing entry categories.
    """
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """
    Admin class for managing entries (news).
    """
    list_display = ('title', 'description', 'published_date', 'link',
                    'category')
    list_filter = ('published_date',)
    search_fields = ('title', 'description')
