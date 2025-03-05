import uuid
from django.db import models
from muhaddis.models import Muhaddis




class Hadis(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    number = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=250)
    uzbek = models.TextField()
    arabic = models.TextField()
    author = models.ForeignKey(Muhaddis, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    data = models.JSONField(default=list, blank=True, null=True)



    def __str__(self):
        return self.title


