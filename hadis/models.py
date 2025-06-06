from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
import uuid
from django.utils import timezone


class Hadis(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    number = models.CharField(max_length=300)
    title = models.CharField(max_length=250)
    uzbek = models.TextField()
    arabic = models.TextField()
    types = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Data(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    hadis = models.ForeignKey(Hadis, on_delete=models.CASCADE, related_name='data_items')
    title = models.CharField(max_length=300, null=True, blank=True)
    text = CKEditor5Field(null=True, blank=True)

    def __str__(self):
        return self.title or f"Data for {self.hadis.title}"

