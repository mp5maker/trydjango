from django.conf.urls import url
from .views import index, IndexView

app_name = "concepts"

urlpatterns = [
    url(r'^', index, name="index"),
    url(r'^home/', IndexView.as_view(), name="home"),
]
