from django.urls import path
from .views import NewsList, CurrentNews


urlpatterns = [
    path('news/', NewsList.as_view()),
    path('news/<int:pk>', CurrentNews.as_view()),
]