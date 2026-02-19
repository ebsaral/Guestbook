from django.db.models import OuterRef, Subquery
from rest_framework import viewsets
from rest_framework.response import Response

from entry.models import Entry
from .models import User
from .serializers import UsersSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UsersSerializer

    def list(self, request):
        # Attach latest entry to each user to be used in a subquery
        latest_entry = Entry.objects.filter(
            user=OuterRef('pk')
        ).order_by('-created_at')

        # For viewing, only id is enough
        users = User.objects.only('id').annotate(
            last_subject=Subquery(latest_entry.values('subject')[:1]),
            last_message=Subquery(latest_entry.values('message')[:1]),
        )

        serializer = UsersSerializer(users, many=True)

        return Response({
            "users": serializer.data
        })