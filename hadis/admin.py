from django.contrib import admin
from .models import *

@admin.register(Hadis)
class HadisAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(HadisData)
class HadisDataAdmin(admin.ModelAdmin):
    list_display = ['title']
