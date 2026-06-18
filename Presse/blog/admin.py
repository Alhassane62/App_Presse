from django.contrib import admin
from .models import *
# Register your models here.


#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titre_article",
        "description",
        "auteur",
        "date_publication"
    )
    
    #list_filter = ("Date")
    #search_fields = ("Auteur")
    
    
@admin.register(Auteur)
class Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom",
        "prenom",
        "sexe",
        "mail",
        "telephone"
    )

