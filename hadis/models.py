import uuid

from django.db import models

from muhaddis.models import Muhaddis


class Hadis(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    uzbek = models.TextField()
    arabic = models.TextField()
    author = models.ForeignKey(Muhaddis, on_delete=models.CASCADE)
    description = models.TextField()



    def __str__(self):
        return self.title
