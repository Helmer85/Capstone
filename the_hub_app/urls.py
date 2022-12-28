from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name = 'news'),
    path('about/', views.about, name = 'about'),
    path('social/', views.social, name = 'social'),
    path('sports/', views.sports, name = 'sports'),
    path('technology/', views.technology, name = 'technology'),
    path('login/', views.login, name='login'),
    path('reddit/', views.reddit, name='reddit'),
    path('twitter/', views.twitter, name= 'twitter'),
    path('games/', views.games, name='games')
]
