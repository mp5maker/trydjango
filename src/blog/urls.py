from django.conf.urls import url
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView
)

app_name = "blog"

urlpatterns = [
    url(r'^article-list/', ArticleListView.as_view(), name="article-list"),
    url(r'^article-detail/(?P<pk>[0-9]+)', ArticleDetailView.as_view(), name="article-detail"),
    url(r'^article-create/', ArticleCreateView.as_view(), name="article-create"),
    url(r'^article-update/(?P<pk>[0-9]+)', ArticleUpdateView.as_view(), name="article-update"),
    url(r'^article-delete/(?P<pk>[0-9]+)', ArticleDeleteView.as_view(), name="article-delete")
]
