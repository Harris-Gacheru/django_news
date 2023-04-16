from django.urls import path
from . import views

urlpatterns = [
    # category
    path('categories/', views.CategoriesAPI.as_view(), name='categories'),
    path('categories/add/', views.CategoryCreateAPI.as_view(), name='add category'),
    path('categories/<int:pk>', views.CategoryAPI.as_view(), name='category'),
    # articles
    path('articles/', views.ArticlesAPI.as_view(), name='articles'),
    path('articles/add/', views.ArticleCreateAPI.as_view(), name='add articles'),
    path('articles/<int:pk>', views.ArticleAPI.as_view(), name='article'),
]