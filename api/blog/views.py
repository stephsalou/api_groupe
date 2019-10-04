
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Categorie ,SousCategorie , Article ,Commentaire
from .serializer import CategorieSerializer , SousCategorieSerializer , ArticleSerializer , CommentaireSerializer
from rest_framework import filters
from rest_framework import viewsets


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])



class CategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
        
class SousCategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer
  
            
class ArticleViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
   

class CommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
  