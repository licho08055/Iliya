
 
from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView
)
    
    


app_name = 'blog'
urlpatterns = [
    
    
   path('',ArticleListView.as_view(),name='blog'),
   path('<int:id>/',ArticleDetailView.as_view(),name='blog'),
   path('create/',ArticleCreateView.as_view(),name='blog'),
   path('<int:id>/update/',ArticleUpdateView.as_view(),name='blog'),
   path('<int:id>/delete/', ArticleDeleteView.as_view(), name='blog'),
    
] 