from django.conf.urls import url

from .views import (home, contact, about)

urlpatterns = [
    url(r'^home/', home, name="home"),
    url(r'^contact/', contact, name="contact"),
    url(r'^about/', about, name="about"),
]
