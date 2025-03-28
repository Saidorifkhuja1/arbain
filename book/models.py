import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from writer.models import Writer


class Book(models.Model):
    STATUS_CHOICES = [
        ('book', 'KITOB VA RISOLALAR'),
        ('article', 'MAQOLA'),
        ('manuscript', 'QO\'LYOZMA'),
    ]
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=STATUS_CHOICES, default='book')
    pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])], blank=True, null=True)
    cover_image = models.ImageField(upload_to='books/covers/', null=True, blank=True)


    def __str__(self):
        return self.title


