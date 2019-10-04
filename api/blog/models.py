from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categorie/')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categories')
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='souscategorie/')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
class Article(models.Model):
    souscategorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, related_name='souscategories')
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='article/')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    description = models.TextField()
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username