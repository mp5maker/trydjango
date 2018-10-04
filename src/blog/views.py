from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    # By Default it looks for appname/<modelname>_list
    # blog/article-list

    # Overriding the the template
    template_name = 'blog/articles/article_list.html' 
    queryset = Article.objects.all() 
