from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesAPI.as_view(), name='categories'),
    path('categories/add/', views.CategoryCreateAPI.as_view(), name='add category'),
    path('categories/<int:pk>', views.CategoryAPI.as_view(), name='category'),
]