from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at', 'author_id', 'category')

list_models = [models.Article, models.Category]
admin.site.register(list_models)