from django.contrib import admin
from .models import Muhaddis

@admin.register(Muhaddis)
class MuhaddisAdmin(admin.ModelAdmin):
    list_display = ['name']

