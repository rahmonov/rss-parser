from rest_framework import serializers

from rss.models import Entry, EntryCategory


class EntryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryCategory
        fields = ('pk', 'name')


class EntrySerializer(serializers.ModelSerializer):
    category = EntryCategorySerializer()

    class Meta:
        model = Entry
        fields = ('pk', 'title', 'description', 'link', 'published_date',
                  'category')

