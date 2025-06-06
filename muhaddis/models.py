import uuid

from django.db import models

class Muhaddis(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='muhaddis/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

