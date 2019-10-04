from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset ,SousCategorieViewset,ArticleViewset,CommentaireViewset


router = DefaultRouter()
router.register('categorie', CategorieViewset, base_name='categorie')
router.register('sous_category',SousCategorieViewset,base_name='sous_categorie')
router.register('article',ArticleViewset,base_name='article')
router.register('commentaire',CommentaireViewset,base_name='commentaire')
urlpatterns = [

]

urlpatterns += router.urls