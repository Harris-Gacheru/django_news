from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(verbose_name='Category Name', max_length=255)
    description = models.TextField(verbose_name='Category Description')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name='Article Title', max_length=255)
    published_at = models.DateField(verbose_name="Publish Date")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title