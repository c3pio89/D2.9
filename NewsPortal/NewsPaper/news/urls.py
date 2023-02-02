from django.urls import path
from .views import NewsList, CurrentNews, ArticlesList, CurrentArticles, news, CurrentPost, search

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', CurrentNews.as_view()),
    path('articles/', ArticlesList.as_view()),
    path('articles/<int:pk>', CurrentArticles.as_view()),
    path('post/', news.as_view()),
    path('post/<int:pk>', CurrentPost.as_view()),
    path('search/', search.as_view()),
]