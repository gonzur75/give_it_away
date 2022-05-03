from django.contrib import admin

from . import models
from .models import Category


@admin.register(models.Institution)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type')
    list_filter = ['categories']
    search_fields = ['name']



admin.site.register(models.Category)
admin.site.register(models.Donation)
