from django.contrib import admin
from django import forms
from .models import Hadis, Data
from django_ckeditor_5.widgets import CKEditor5Widget



class DataAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditor5Widget(config_name='extended'))

    class Meta:
        model = Data
        fields = '__all__'



class DataInline(admin.StackedInline):
    model = Data
    form = DataAdminForm
    extra = 0


class HadisAdminForm(forms.ModelForm):
    uzbek = forms.CharField(widget=CKEditor5Widget(config_name='extended'))
    arabic = forms.CharField(widget=CKEditor5Widget(config_name='extended'))

    class Meta:
        model = Hadis
        fields = '__all__'



@admin.register(Hadis)
class HadisAdmin(admin.ModelAdmin):
    form = HadisAdminForm
    list_display = ['title', 'number', 'author']
    list_filter = ['types', 'author']
    search_fields = ['title', 'description', 'uzbek', 'arabic']
    inlines = [DataInline]

