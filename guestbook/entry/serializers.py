
from rest_framework import serializers

from user.models import User
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Entry
        fields = ['name', 'user', 'subject', 'message']

    def get_user(self, obj):
        return obj.user.name
    
    def create(self, validated_data):
        name = validated_data.pop("name")
        user, _ = User.objects.get_or_create(name=name)
        entry = Entry.objects.create(user=user, **validated_data)
        return entry