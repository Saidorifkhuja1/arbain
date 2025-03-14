from django import forms
from .models import Videos
from django.contrib import admin



class VideosAdminForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'
        widgets = {
            'video': forms.ClearableFileInput(attrs={'accept': 'video/*'}),
        }

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    form = VideosAdminForm
    list_display = ['title']