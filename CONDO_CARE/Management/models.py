from django.db import models
from django.utils import timezone

class Announcement(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    post_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





