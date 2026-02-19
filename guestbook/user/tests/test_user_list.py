import pytest
from rest_framework.test import APIClient

from user.models import User
from entry.models import Entry


@pytest.mark.django_db
class TestUserList:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/users/"

    def test_user_last_entry(self):
        user = User.objects.create(name="Emin")

        Entry.objects.create(user=user, subject="A1", message="M1")
        Entry.objects.create(user=user, subject="A2", message="M2")

        response = self.client.get(self.url)

        assert response.status_code == 200
        assert len(response.data["users"]) == 1

        user_data = response.data["users"][0]

        assert user_data["username"] == f"Emin"
        assert user_data["last_entry"] == "A2 | M2"

    def test_multiple_users(self):
        user1 = User.objects.create(name="User1")
        user2 = User.objects.create(name="User2")

        Entry.objects.create(user=user1, subject="A1", message="M1")
        Entry.objects.create(user=user1, subject="A2", message="M2")
        Entry.objects.create(user=user2, subject="B1", message="M1")

        response = self.client.get(self.url)

        assert response.status_code == 200
        assert len(response.data["users"]) == 2

        users_dict = {u["username"]: u for u in response.data["users"]}

        assert users_dict[f"User1"]["last_entry"] == "A2 | M2"
        assert users_dict[f"User2"]["last_entry"] == "B1 | M1"
