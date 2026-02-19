from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField("Created Date", auto_now_add=True)