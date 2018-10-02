# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request, *args, **kwargs): # *args, **kwargs
    # print(args, kwargs) # see the wsgi requests
    #  (<WSGIRequest: GET '/'>,), {})
    
    # Therefore, we can see a request is coming
    # print(request.user) prints out the which user sent the request
    # Great for authentication, login
    
    # return HttpResponse("<h1>Hello World</h1>") #string of HTML Code
    return render(request, "home.html", {})

def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about(request, *args, **kwargs):
    context = {
        "address": [
            'Dhanmondi',
            'Gulshan',
            'Uttara'
        ]
    }
    return render(request, "about.html", context) 

def product_detail(request, *args, **kwargs):
    obj = Product.objects.get(pk=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description
    # }
    context = {
        "obj": obj
    }
    return render(request, 'products/detail.html', context)

def product_form_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        "form": form
    }
    return render(request, "products/product_form_view.html", context)