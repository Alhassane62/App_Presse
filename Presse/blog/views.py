from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *


# listes des articles
def list_article(request):
    articles = Article.objects.all()
    return render(request, 'blog/listeblog.html', {'articles': articles})

# details des articles 
def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detailarticle.html', {'article':article})




# creer un article de blog
def create_article(request):        
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_article')
    else:
        form = ArticleForms()
        
    return render(request, 'blog/createarticle.html', {'form': form})

# modifier un article de blog
def update_article(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleForms(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('list_article')

    else:
        form = ArticleForms(instance=article)

    return render(
        request,
        'blog/updatearticle.html',
        {
            'form': form,
            'article': article
        }
    )
    
    
# delete article 
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == "POST":
        article.delete()
        return redirect('list_article')

    return render(request, 'blog/deletearticle.html', {'article':article})



#list e des auteurs
def list_auteur(request):
    auteurs = Auteur.objects.all()
    context = {
        'auteurs': auteurs
    }
    return render(request, 'auteur/listeauteur.html', context)
    
    
# details auteur 
def detail_auteur(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    context = {
        'auteur': auteur
    }
    return render(request, 'auteur/detailauteur.html', context)

# creer un auteur 
def create_auteur(request):
    if request.method == "POST":
        form = AuteurForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_auteur')
    else:
        form = AuteurForms()
    context = {
        'form': form
    }
    return render(request, 'auteur/createauteur.html', context)


# mettre a jour 
def update_auteur(request, pk):
    
    auteur = get_object_or_404(Auteur, pk=pk)
    
    if request.method == "POST":
        form = AuteurForms(request.POST, instance = auteur)
        if form.is_valid():
            form.save()
            return redirect('list_auteur')
    else:
        form = AuteurForms(instance=auteur)
        
    context = {
        'form': form,
        'auteur': auteur
    }
    return render(request, 'auteur/updateauteur.html', context)

