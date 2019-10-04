from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import Categorie , SousCategorie , Article , Commentaire


class CommentaireSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields= '__all__'

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    articles = CommentaireSerializer(many=True,required=False)

    class Meta:
        model = Article
        fields = '__all__'

class SousCategorieSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    souscategories = ArticleSerializer(many=True, required=False)

    class Meta:
        model = SousCategorie
        fields = '__all__'

class CategorieSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    categories =SousCategorieSerializer(many=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'




