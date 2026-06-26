from django.urls import path
from .import views 
urlpatterns = [
    path('', views.list_article, name="list_article"),
    path('detail/<int:pk>/', views.detail_article, name="detail_article"),
    path('create', views.create_article, name="create_article"),
    path('<int:pk>/modifier', views.update_article, name="update_article"),
    path('<int:pk>/delete/', views.delete_article, name = "delete_article"),
    
    
    # url auteur 
    path('liste/auteur', views.list_auteur, name="list_auteur"), 
    path('<int:pk>/detail', views.detail_auteur, name = "detail_auteur"),
    path('create/auteur', views.create_auteur, name="create_auteur"),
    path('<int:pk>/update/article', views.update_auteur, name="update_auteur"),
    
    
]
