from django.db import models


class Entry(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField("Created Date", auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["user", "-created_at"]),
        ]