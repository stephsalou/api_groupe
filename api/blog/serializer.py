from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import Categorie , SousCategorie , Article , Commentaire
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# ...
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

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




