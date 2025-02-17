from django.contrib import admin
from .models import Hadis

@admin.register(Hadis)
class HadisAdmin(admin.ModelAdmin):
    list_display = ['title']


