from django.db import models
from django.utils import timezone  
from auteur.models import Auteur


class Article(models.Model):
    titre_article = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=True)
    auteur = models.ForeignKey("Auteur", on_delete=models.CASCADE)
    date_publication = models.DateTimeField(default=timezone.now) 
     
    def __str__(self):
        return self.titre_article


    