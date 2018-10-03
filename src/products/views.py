# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .forms import ProductForm, ProductRawForm

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
    if form.is_valid(): # Checks the validation of the form
        form.save() # Saves the data into the database
        form = ProductForm() # Clears the field of the form after the form is sent
    
    context = {
        "form": form
    }
    return render(request, "products/product_form_view.html", context)

def product_form_raw(request, *args, **kwargs):
    my_form = ProductRawForm()
    if request.method == "POST":
        my_form = ProductRawForm(request.POST)
        if my_form.is_valid():
            print my_form.cleaned_data 
            Product.objects.create(**my_form.cleaned_data)
        else:
            print my_form.errors
    else:
        my_form = ProductRawForm(None)
    context = {
        "form": my_form
    }
    return render(request, 'products/product_form_raw.html', context)