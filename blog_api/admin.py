from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(models.Category, CategoryAdmin)