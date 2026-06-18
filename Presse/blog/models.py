from django.db import models
from django.utils import timezone  

class Article(models.Model):
    titre_article = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=True)
    auteur = models.ForeignKey("Auteur", on_delete=models.CASCADE)
    date_publication = models.DateTimeField(default=timezone.now) 
     
    def __str__(self):
        return self.titre_article


class Auteur(models.Model):
    Homme = 'H'
    Femme = 'F'
    choices_sexe = [(Homme,'homme'),
                    (Femme, 'femme')
                ]
    
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=100, null=False)
    sexe = models.CharField(choices=choices_sexe, default='')
    mail = models.CharField(max_length=20, null=False)
    telephone = models.CharField(max_length=15)
    
    
    def __str__(self):
        return f"{self.nom} {self.prenom}--{self.telephone}"
    
    
    class Meta:
        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    