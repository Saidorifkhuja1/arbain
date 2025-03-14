import uuid
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_video_file_extension(value):
    valid_extensions = ['.mp4', '.avi', '.mov', '.mkv']
    if not any([value.name.lower().endswith(ext) for ext in valid_extensions]):
        raise ValidationError("Unsupported file extension. Please upload a video file.")

class Videos(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='videos/', max_length=10000000)
    video = models.FileField(upload_to='videos/', validators=[validate_video_file_extension], max_length=10000000)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

