from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    template_name = 'NewsList.html'
    context_object_name = 'NewsList'
    def get_queryset(self):
        return Post.objects.filter(categoryType='NW').order_by('dateCreation')


class CurrentNews(DetailView):
    model = Post
    template_name = 'CurrentNews.html'
    context_object_name = 'CurrentNews'
    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')

class ArticlesList(ListView):
    model = Post
    template_name = 'ArticlesList.html'
    context_object_name = 'ArticlesList'
    def get_queryset(self):
        return Post.objects.filter(categoryType='AR').order_by('dateCreation')


class CurrentArticles(DetailView):
    model = Post
    template_name = 'CurrentArticles.html'
    context_object_name = 'CurrentArticles'
    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')

class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.filter().all()

class CurrentPost(DetailView):
    model = Post
    template_name = 'CurrentPost.html'
    context_object_name = 'CurrentPost'
    def get_queryset(self):
        return Post.objects.filter().all()

class search(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context