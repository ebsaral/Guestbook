import pytest
from rest_framework.test import APIClient

from user.models import User
from entry.models import Entry


@pytest.mark.django_db
class TestEntryCreate:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/entries/"

    def test_create_entry_creates_new_user(self):
        payload = {
            "name": "Emin",
            "subject": "subject_1",
            "message": "message_1"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == 201
        assert User.objects.count() == 1
        assert Entry.objects.count() == 1
        assert User.objects.first().name == "Emin"

    def test_create_entry_reuses_existing_user(self):
        user = User.objects.create(name="Emin")

        payload = {
            "name": "Emin",
            "subject": "subject_2",
            "message": "message_2"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == 201
        assert User.objects.count() == 1
        assert Entry.objects.count() == 1
        assert Entry.objects.first().user == user
