from django.contrib import admin
from .models import *

@admin.register(Hadis)
class HadisAdmin(admin.ModelAdmin):
    list_display = ['title']
    raw_id_fields = ['data']  # Enables a lookup UI for HadisData
    autocomplete_fields = ['data']  # Enables search functionality for HadisData

@admin.register(HadisData)
class HadisDataAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']