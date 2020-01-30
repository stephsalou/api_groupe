from django.urls import path,include
from .views import basic_seeder
from rest_framework.routers import DefaultRouter
from .views import CategorieViewset ,SousCategorieViewset,ArticleViewset,CommentaireViewset,UserCreate
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'categories', CategorieViewset, base_name='categories')
router.register(r'user',UserCreate,base_name='user')
souscategorie_router = routers.NestedSimpleRouter(router, r'categories', lookup='categorie')
souscategorie_router.register(r'sous_categories', SousCategorieViewset, base_name='sous_categories')

article_router = routers.NestedSimpleRouter(souscategorie_router, r'sous_categories', lookup='souscategorie')
article_router.register(r'articles', ArticleViewset, base_name='articles')

commentaire_router = routers.NestedSimpleRouter(article_router, r'articles', lookup='article')
commentaire_router.register(r'commentaire', CommentaireViewset, base_name='commentaires')
# router = DefaultRouter()
# router.register('categorie', CategorieViewset, base_name='categorie')
# router.register('sous_category',SousCategorieViewset,base_name='sous_categorie')
# router.register('article',ArticleViewset,base_name='article')
# router.register('commentaire',CommentaireViewset,base_name='commentaire')
urlpatterns = [
    # path('basicfake/', basic_seeder),
]

urlpatterns += router.urls
urlpatterns += souscategorie_router.urls
urlpatterns += article_router.urls
urlpatterns += commentaire_router.urls