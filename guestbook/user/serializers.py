from rest_framework import serializers

from user.models import User


class UsersSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    last_entry = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "last_entry"]

    def get_username(self, obj):
        return obj.name

    def get_last_entry(self, obj):
        return f"{obj.last_subject} | {obj.last_message}"