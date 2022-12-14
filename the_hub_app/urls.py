from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name = 'news'),
    path('about/', views.about, name = 'about'),
    path('social/', views.social, name = 'social'),
    path('sports/', views.sports, name = 'sports'),
    path('sports_news/', views.sports_news, name = 'sports_news'),
]
