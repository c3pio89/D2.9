from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
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

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    form_class = PostForm
    model = Post
    template_name = 'NewsCreate.html'
    success_url = '/news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'NewsEdit.html'
    success_url = '/news/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    model = Post
    template_name = 'NewsDelete.html'
    success_url = '/news/'

class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('articles.add_post')
    form_class = PostForm
    model = Post
    template_name = 'ArticlesCreate.html'
    success_url = '/articles/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

class ArticlesEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('articles.change_post')
    form_class = PostForm
    model = Post
    template_name = 'ArticlesEdit.html'
    success_url = '/articles/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)

class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('articles.delete_post')
    model = Post
    template_name = 'ArticlesDelete.html'
    success_url = '/articles/'
