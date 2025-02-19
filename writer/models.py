from django.db import models
import uuid



class Writer(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='writer/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name




