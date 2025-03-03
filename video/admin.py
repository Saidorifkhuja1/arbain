from django.contrib import admin
from .models import Videos

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['title']

    