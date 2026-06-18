from django.urls import path
from .import views 
urlpatterns = [
    path('', views.list_article, name="list_article"),
    path('detail/<int:pk>/', views.detail_article, name="detail_article"),
    path('create', views.create_article, name="create_article"),
    path('<int:pk>/modifier', views.update_article, name="update_article"),
    path('<int:pk>/delete/', views.delete_article, name = "delete_article"),
    
    
    
]
