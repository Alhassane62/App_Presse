from django import forms
from .models import *

class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
        


class AuteurForms(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'
        
    