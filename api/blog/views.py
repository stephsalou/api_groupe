import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Categorie ,SousCategorie , Article ,Commentaire
from .serializer import CategorieSerializer , SousCategorieSerializer , ArticleSerializer ,UserSerializer, CommentaireSerializer
from rest_framework import filters
from rest_framework import viewsets
from .models import *

# Create your views here.
class UserCreate(viewsets.ModelViewSet):
    # authentication_classes = ()
    # permission_classes = ()
    serializer_class=UserSerializer
    def get_queryset(self):
        queryset = User.objects.filter()

        return queryset
    
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])



class CategorieViewset(viewsets.ViewSet):

    def list(self, request):
        queryset = Categorie.objects.filter()
        serializer = CategorieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Categorie.objects.filter()
        categorie = get_object_or_404(queryset, pk=pk)
        serializer = CategorieSerializer(souscategorie)
        return Response(serializer.data)
    serializer_class = CategorieSerializer
    
        
# class SousCategorieViewset(viewsets.ModelViewSet):
#     filter_backends = (DynamicSearchFilter,)
#     queryset = SousCategorie.objects.all()
#     serializer_class = SousCategorieSerializer

class SousCategorieViewset(viewsets.ViewSet):
    serializer_class = SousCategorieSerializer
    def list(self, request,categorie_pk):
        print('=====================',categorie_pk,'======================')
        queryset = SousCategorie.objects.filter(categorie=categorie_pk)
        serializer = SousCategorieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,pk=None,categorie_pk=None):
        queryset = SousCategorie.objects.filter(pk=pk,categorie=categorie_pk)
        souscategorie = get_object_or_404(queryset,pk=pk)
        serializer = SousCategorieSerializer(souscategorie)
        return Response(serializer.data)

            
class ArticleViewset(viewsets.ViewSet):
    def list(self, request,categorie_pk,souscategorie_pk):
        queryset = Article.objects.filter(souscategorie__categorie=categorie_pk,souscategorie=souscategorie_pk)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,categorie_pk=None,souscategorie_pk=None, pk=None):
        queryset = Article.objects.filter(souscategorie__categorie=categorie_pk,souscategorie=souscategorie_pk,pk=pk)
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    serializer_class = ArticleSerializer

class CommentaireViewset(viewsets.ViewSet):
    def list(self, request,categorie_pk,souscategorie_pk, article_pk):
        queryset = Commentaire.objects.filter(article__souscategorie__categorie=categorie_pk,article__souscategorie=souscategorie_pk,article=article_pk)
        serializer = CommentaireSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,categorie_pk=None,souscategorie_pk=None, article_pk=None, pk=None):
        queryset = Commentaire.objects.filter(article__souscategorie__categorie=categorie_pk,article__souscategorie=souscategorie_pk,article=article_pk,pk=pk)
        commentaire = get_object_or_404(queryset, pk=pk)
        serializer = CommentaireSerializer(commentaire)
        return Response(serializer.data)
    serializer_class = CommentaireSerializer

###  Seeder

Images = [os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)]+ [os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)]

def getimage():
    global Images
    img=images[randint(0,len(images)-1)]
    img = open(img,'rb')
    return img


def basic_seeder():
    from django.core.files import File
    seeder = Seed.seeder()
    seeder.add_entity(Categorie, 10,{
        'image': File(getimage())
    })
    seeder.add_entity(User, 10)
    seeder.add_entity(SousCategorie, 30,{
        'image': File(getimage())
    })
    seeder.add_entity(Article, 50,{
        'image': File(getimage())
    })
    seeder.add_entity(Commentaire, 100)
    inserted_pks = seeder.execute()
