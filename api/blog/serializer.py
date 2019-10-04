from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import Categorie , SousCategorie , Article , Commentaire



class CategorieSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class SousCategorieSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    categories = CategorieSerializer(many=True, required=True)

    class Meta:
        model = SousCategorie
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    souscategorie = SousCategorieSerializer(many=True,required=True)

    class Meta:
        model = Article
        fields = '__all__'

class CommentaireSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    articles = ArticleSerializer(many=True,required=False)
    class Meta:
        model = Commentaire
        fields= '__all__'