from django.http import Http404
from .serializer import CategorySerializer, ArticleSerializer
from rest_framework import response,views, status, permissions
from . import models
from users.authentication import CustomAuthentication

class CategoriesAPI(views.APIView):
    def get(self, request):
        categories = models.Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        if len(categories) == 1:
            return response.Response({'message': 'Category found', 'data': serializer.data}, status=status.HTTP_200_OK)
        elif len(categories) > 0:
            return response.Response({'message': 'Categories found', 'data': serializer.data}, status=status.HTTP_200_OK)
        return response.Response({'message': 'Categories not found', 'data': []}, status=status.HTTP_404_NOT_FOUND)

class CategoryCreateAPI(views.APIView):
    authentication_classes = (CustomAuthentication, )
    permission_classes = (permissions.IsAdminUser, )

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryAPI(views.APIView):
    def get_category_by_pk(self, pk):
        try:
            return models.Category.objects.get(pk=pk)
        except models.Category.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        category = self.get_category_by_pk(pk)
        serializer = CategorySerializer(category)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        category = self.get_category_by_pk(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return response.Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = self.get_category_by_pk(pk)
        category.delete()
        return response.Response({'message': 'Deleted successfully'}, status=status.HTTP_200_OK)
    
class ArticlesAPI(views.APIView):
    authentication_classes = (CustomAuthentication, )

    def get(self, request):
        articles = models.Article.objects.filter(author_id=request.user.id)
        serializer = ArticleSerializer(articles, many=True)
        if len(articles) == 1:
            return response.Response({'message': 'Article found', 'data': serializer.data}, status=status.HTTP_200_OK)
        elif len(articles) > 0:
            return response.Response({'message': 'Articles found', 'data': serializer.data}, status=status.HTTP_200_OK)
        return response.Response({'message': 'Articles not found', 'data': []}, status=status.HTTP_404_NOT_FOUND)
    
class ArticleAPI(views.APIView):
    def get_article_by_pk(self, pk):
        try:
            return models.Article.objects.get(pk=pk)
        except models.Article.DoesNotExist:
            return response.Response({'error': 'Article does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        article = self.get_article_by_pk(pk)
        serializer = ArticleSerializer(article)
        return response.Response({'message': 'Article found', 'data': serializer.data})
        
    def put(self, request, pk):
        article = self.get_article_by_pk(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Updated successfully', 'data': serializer.data})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_article_by_pk(pk=pk)
        article.delete()
        return response.Response({'message': 'Deleted successfully'})
    
class ArticleCreateAPI(views.APIView):
    authentication_classes = (CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        print('user',request.user.id)
        data = request.data            
        data["author_id"] = request.user.id
        serializer = ArticleSerializer(data=data)
        print('data', serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'Added successfully', 'data': serializer.data})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)