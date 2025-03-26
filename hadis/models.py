import uuid
from django.db import models
from muhaddis.models import Muhaddis

#
# class Data(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
#     title = models.CharField(max_length=300, null=True, blank=True)
#     text = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.title





class Hadis(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    number = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=250)
    uzbek = models.TextField(null=True, blank=True)
    arabic = models.TextField(null=True, blank=True)
    types = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    data = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.title


