from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.liste_articles, name='liste_articles'),
    path('articles/<int:id>/', views.detail_article, name='detail_article'),
]