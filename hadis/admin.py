# from django.contrib import admin
# from .models import Hadis, Data
#
#
# class DataInline(admin.StackedInline):
#     model = Data
#     extra = 1
#
#
# @admin.register(Hadis)
# class HadisAdmin(admin.ModelAdmin):
#     list_display = ['title', 'number', 'author']
#     list_filter = ['types', 'author']
#     search_fields = ['title', 'description', 'uzbek', 'arabic']
#     inlines = [DataInline]
from django.contrib import admin
from .models import Hadis, Data
from ckeditor.widgets import CKEditorWidget
from django import forms

class DataAdminForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(config_name='basic'),
        }

class DataInline(admin.StackedInline):
    model = Data
    extra = 1
    form = DataAdminForm

class HadisAdminForm(forms.ModelForm):
    class Meta:
        model = Hadis
        fields = '__all__'
        widgets = {
            'uzbek': CKEditorWidget(config_name='default'),
        }

@admin.register(Hadis)
class HadisAdmin(admin.ModelAdmin):
    form = HadisAdminForm
    list_display = ['title', 'number', 'author']
    list_filter = ['types', 'author']
    search_fields = ['title', 'description', 'uzbek', 'arabic']
    inlines = [DataInline]

