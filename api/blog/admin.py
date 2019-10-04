from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class SousCategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'categorie',
        'statut',
        'date_add',
        'date_update',
        'id',
        'categorie',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'souscategorie',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'souscategorie',
        'statut',
        'date_add',
        'date_update',
        'id',
        'souscategorie',
        'nom',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'user',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'article',
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'article',
        'user',
        'description',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.SousCategorie, SousCategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
