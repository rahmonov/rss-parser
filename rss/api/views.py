# -*- coding: utf-8 -*-
import json

from rss.tasks import render_to_pdf
try:
    import StringIO
    StringIO = StringIO.StringIO
except Exception:
    from io import StringIO

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rss.api.serializers import EntrySerializer, EntryCategorySerializer
from rss.models import Entry, EntryCategory


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryCategoryList(generics.ListCreateAPIView):
    queryset = EntryCategory.objects.all()
    serializer_class = EntryCategorySerializer

    def get(self, request, *args, **kwargs):
        try:
            category_name = request.query_params['catName']
        except KeyError:
            return super(EntryCategoryList, self).get(request, *args, **kwargs)

        categories = EntryCategory.objects.filter(
            name__icontains=category_name)
        serialized_categories = EntryCategorySerializer(categories, many=True)

        return Response(serialized_categories.data, status=status.HTTP_200_OK)


class FilterEntry(APIView):
    def get(self, request):
        from_date = json.loads(request.query_params.get('fromDate', ''))
        to_date = json.loads(request.query_params.get('toDate', ''))
        category_id = request.query_params.get('categoryId', '')
        entries = Entry.objects.all()

        if not from_date and not to_date and not category_id:
            entries = EntrySerializer(entries, many=True).data
            return Response({'entries': entries}, status=status.HTTP_200_OK)

        if from_date:
            entries = entries.filter(published_date__gte=from_date)

        if to_date:
            entries = entries.filter(published_date__lte=to_date)

        if category_id:
            entries = entries.filter(category__pk=category_id)

        serialized_entries = EntrySerializer(entries, many=True).data

        return Response({'entries': serialized_entries},
                        status=status.HTTP_200_OK)


@api_view(('POST',))
def send_report(request):
    try:
        to_email = request.data['email']
        entry_ids = request.data['entryIds']
    except KeyError:
        return Response({'message': 'Wrong input'},
                        status=status.HTTP_400_BAD_REQUEST)
    entries = Entry.objects.filter(pk__in=entry_ids)

    render_to_pdf.delay('entries.html', {
        'pagesize': 'A4',
        'title': 'Digest Report',
        'entries': entries}, to_email)

    return Response(status=status.HTTP_200_OK)



