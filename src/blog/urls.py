from django.conf.urls import url
from .views import ArticleListView

urlpatterns = [
    url(r'^article-list/', ArticleListView.as_view(), name="article-list")
]
