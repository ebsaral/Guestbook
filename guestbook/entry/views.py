from rest_framework import pagination, viewsets
from rest_framework.response import Response

from .models import Entry
from .serializers import EntrySerializer

class EntryPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "page_size": self.get_page_size(self.request),
            "total_pages": self.page.paginator.num_pages,
            "current_page_number": self.page.number,
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
            "entries": data
        })


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by("-created_at")
    serializer_class = EntrySerializer
    pagination_class = EntryPagination