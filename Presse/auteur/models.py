from django.db import models

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
