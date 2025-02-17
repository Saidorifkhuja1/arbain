import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from writer.models import Writer


class Book(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)
    description = models.TextField()
    pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])], blank=True, null=True)
    cover_image = models.ImageField(upload_to='books/covers/', null=True, blank=True)


    def __str__(self):
        return self.title


