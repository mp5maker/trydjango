from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
class ArticleListView(ListView):
    # By Default it looks for appname/<modelname>-list
    # blog/article-list

    # Overriding the the template
    template_name = 'blog/articles/article_list.html' 
    queryset = Article.objects.all() 

class ArticleDetailView(DetailView):
    template_name = "blog/articles/article_detail.html"
    # Queryset limits the chocies available for the detail view
    # This accepts primary key

    # Overriding Get Object
    # /blog/article-detail/(numbers)
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    template_name = "blog/articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form
    
    # How to override the success url
    # def get_success_url(self):
    #     return '/blog/article-list'
    success_url = "/blog/article-list"


class ArticleUpdateView(UpdateView):
    template_name = "blog/articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)

    # How to override the success url
    # def get_success_url(self):
    #     return '/blog/article-list'
    success_url = "/blog/article-list"


class ArticleDeleteView(DeleteView):
    template_name = "blog/articles/article_delete.html"
    # form_class = ArticleModelForm
    # queryset = Article.objects.all()
    # success_url = "/blog/article-list/"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
    
    def get_success_url(self):
        return reverse('blog:article-list')
