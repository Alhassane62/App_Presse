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