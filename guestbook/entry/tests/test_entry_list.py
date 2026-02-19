import pytest
from rest_framework.test import APIClient

from user.models import User
from entry.models import Entry


@pytest.mark.django_db
class TestEntryList:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/entries/"

    def test_entry_pagination(self):
        user = User.objects.create(name="TestUser")

        for i in range(5):
            Entry.objects.create(
                user=user,
                subject=f"subject_{i}",
                message=f"message_{i}"
            )

        response = self.client.get(self.url)

        assert response.status_code == 200
        assert response.data["count"] == 5
        assert len(response.data["entries"]) == 3  # default page_size
        assert response.data["current_page_number"] == 1
