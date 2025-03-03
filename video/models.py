import uuid
from django.db import models
from django.utils import timezone

class Videos(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='videos/')
    video = models.ImageField(upload_to='videos/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

