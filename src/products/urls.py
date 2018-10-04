from django.conf.urls import url

from .views import (
    product_detail,
    product_form_view,
    product_form_raw, product_initial_data,
    dynamic_lookup_view, product_delete_view,
    product_list_view
)

# This namespaces the url
app_name = "products"

urlpatterns = [
    url(r'^detail/', product_detail, name="product_detail"),
    url(r'^create/', product_form_view, name="product_form_view"),
    url(r'^rawcreate/', product_form_raw, name="product_form_raw"),
    url(r'^initialdata/', product_initial_data, name="product_initial_data"),
    url(r'^dynamic-lookup/(?P<product_id>[0-9]+)/', dynamic_lookup_view, name="dynamic_lookup_view"),
    url(r'^delete/(?P<product_id>[0-9]+)/', product_delete_view, name="product_delete_view"),
    url(r'^product-list/', product_list_view, name="product_list_view")
]
