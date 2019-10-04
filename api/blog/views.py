
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Categorie ,SousCategorie , Article ,Commentaire
from .serializer import CategorieSerializer , SousCategorieSerializer , ArticleSerializer , CommentaireSerializer
from rest_framework import filters
from rest_framework import viewsets
from .models import *

# Create your views here.


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])



class CategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    @detail_route(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise Exception('Request has no resource file attached')
        categorie = Categorie(request.data)
        categorie.image= file
        categorie.save()
        
class SousCategorieViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = SousCategorie.objects.all()
    serializer_class = SousCategorieSerializer
    @detail_route(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise Exception('Request has no resource file attached')
        souscategorie = Categorie(request.data)
        SousCategorie.image= file
        SousCategorie.save()
            
class ArticleViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    @detail_route(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise Exception('Request has no resource file attached')
        article = Article(request.data)
        article.image= file
        article.save()


class CommentaireViewset(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    @detail_route(methods=['post'])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise Exception('Request has no resource file attached')
        commentaire = Commentaire(request.data)
        commentaire.image= file
        commentaire.save()


###  Seeder

Images = [os.path.join(settings.BASE_DIR,'static/images/breakfast-'+str(i)+'.jpg') for i in range(1,5)]+ [os.path.join(settings.BASE_DIR,'static/images/lunch-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dinner-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/dessert-'+str(i)+'.jpg') for i in range(1,5)] + [os.path.join(settings.BASE_DIR,'static/images/drink-'+str(i)+'.jpg') for i in range(1,6)]

def getimage()
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
