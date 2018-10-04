## Try Django ##
All thanks to Coding Entrepreneurs

## Operating System ##
Working in Linux Ubuntu 18.04

## Installation ##
```bash
    sudo apt-get install pip
    sudo apt-get install nodejs

    pip install environ
    pip install virtualenvwrapper
    pip install Django==1.11.16

    export WORKON_HOME=~/Envs
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
    source ~/.bashrc
    mkvirtualenv djangoconcepts
```

## Virtual Environment Commands ##
```bash
1. mkvirtualenv [name]
2. rmvirtualenv [name]
3. workon [name]
4. deactivate
```

## Django Admin Command ##
django-admin startproject [name]

## Management Commands ##
* python manage.py migrate
* python manage.py runserver
* python manage.py shell_plus
* python manage.py shell
* python manage.py startapp angular
* python manage.py createsuperuser
* python manage.py makemigration [name]

## Folder Setups [In my current folder] ##
```bash
    mkdir src
    cd src
    django-admin startproject trydjango .
```
## Settings [src/django/settings.py] ##
**1) Where my manage.py file is ?**
```bash
    print BASE_DIR
    In my case,
    /home/photon/Downloads/trydjango/src
```
**2) What is installed app ?**
* All the apps must be entered here INSTALLED_APPS

**3) What is URL CONF ?**
* Url configuration manages all the routes

**4) Where do we store the js, css, html?**
* STATIC_URL

## Create Superuser ##
* Create superuser
```bash
    python manage.py createsuperuser
```

## Create New App ##
* Create new app
```bash
    python manage.py startapp products
```
## Create Model [models.py] and Make Migrations ##
```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField() 
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default="Write Meaningful Description")

```
```bash
    python manage.py makemigrations
    python manage.py migrate
```
## Register in Admin [admin.py] ##
```python
    admin.site.register(*model-name*) 
```
## Python Shell ##
```bash
    python manage.py shell

    from products.models import Product
    
    Read,
    result = Product.objects.all()
    str(result.query)
    print result

    Create,
    Product.objects.create(title="String", description="Ernie Balls", price="8.99", summary="")
```

## Updating the Model ##
* Updating the previous model with new fields with default value to new fields
```python
    class Product(models.Model):
        title       = models.CharField(max_length=120) # max_length is required
        description = models.TextField(blank=True, null=True)
        price       = models.DecimalField(decimal_places=2, max_digits=1000)
        summary     = models.TextField(default="Write Meaningful Description")
        ## Added After two products were added, featured was added
        featured    = models.BooleanField() # null=True, default=True
```
```bash
    python manage.py makemigrations
    
    Choose > Provide a one-off default now
    Press 1
    Type True
    
    python manage.py migrate
```

## Creating a View [views.py] ##
```python 
    from django.http import HttpResponse

    class Home(*args, **kwargs):
        return Response("<h1> Hello World </h1>")
```

## Create a url for the view trydjango[urls.py] ##
```python
    from django.conf.urls import url
    from django.contrib import admin
    from products.views import home

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', home, name="home"),
    ]
```

## Print arguments and keyword arguments[views.py] ##
```python
    class Home(*args, **kwargs):
        print(args, kwargs) # We can see in the server 
        return Response("<h1> Hello World </h1>")
```
```bash
    (<WSGIRequest: GET '/'>,), {})
```
Therefore we can write,
```python
    class Home(request, *args, **kwargs):
        print(args, kwargs) # We can see in the server 
        ## We will see the request
        return Response("<h1> Hello World </h1>")
```

## What can request do ? ##
* We can see the which user sent the request, authentication,login helps
```python
        class Home(request, *args, **kwargs):
        # print(args, kwargs) # We can see in the server 
        # print(request.user) # Requested user info
        return Response("<h1> Hello World </h1>")
```

## Template (views.py) ##
```python
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs): 
    return render(request, "home.html", {})
```

## Templates in src folder ##
```bash
    mkdir templates
```

## Setup Django where templates are (settings.py) ##
```python
    TEMPLATES = [
        {
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        }
    ]
```
## Using Jinja Templates ##
```html
    [Jinja Template Inheritance]
    {% extends 'base.html'}
    {% block content %}
    {% endblock %}

    [Jinja Template Include]
    {% include 'layouts/navbar.html' %}

    [Jinja Template for Loop]
    {% for item in list %}
    {% endfor %}
    We can use *forloop.counter* to count the loop

    [Jinja Template Conditions]
    {% if <<condition>> %}
    {% elif <<condition>> %}
    {% else %}
    {% endif %}
```

## Template Tag Filters ##
* {{ variable | upper }}
* {{ variable | add }}
* {{ variable | slugify }}
* {{ variable | capfirst }}
* {{ variable | safe }}
* {{ variable | striptags }}

## Access the Data through Shell ##
<< Get the Query Set >>
```bash
    from products.models import Product
    obj = Product.objects.all()
    str(obj.query)
    print obj
```
<< Get all the attributes, mthod of a certain object >>
```bash
    from products.models import Product
    obj = Product.objects.get(pk=1)
    dir(obj)
    obj.title
```
## Render Data from the Database ##
1. Write the naming convention of the functions in the view in lowercase
2. Write the name convention of the functions in the model in uppercase

views.py
```python
    from .models import Product 
    def product_detail(request, *args, **kwargs):
    obj = Product.objects.get(pk=1)
    context = {
        "title": obj.title,
        "description": obj.description
    }
    return render(request, 'product/detail.html', context)
```
product/detail.html
```html
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col">
            <h1>Items</h1>
            <div class="information">
                <ul>
                    <li>
                        <span>
                            {{ title }}
                        </span>
                        {% if description != Null and description != '' %}
                        <span>
                            {{ description}}
                        </span>
                        {% else %}
                        <span>
                            Coming Soon
                        </span>
                        {% endif %}
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```
views.py [Improved]
```python
def product_detail(request, *args, **kwargs):
    obj = Product.objects.get(pk=1)
    context = {
        "obj": obj
    }
    return render(request, 'product/detail.html', context)
```

## Changing the location of the template ##
Inside the Product app,
```bash
    mkdir templates
    cd templates 
    mkdir products
    touch detail.html
```
Intentionally making mistake in views.py
```bash
    return render(request, 'productss/detail.html', context)
```

Checking the Template loader post mortem
```bash
django.template.loaders.filesystem.Loader: /home/photon/Downloads/trydjango/src/templates/productss/detail.html 
```
*Comes from the settings*
*'DIRS': [os.path.join(BASE_DIR, 'templates')]*


```bash
django.template.loaders.app_directories.Loader: /home/photon/Downloads/trydjango/src/products/templates/productss/detail.html
```
*Comes from the products app*

```bash
django.template.loaders.app_directories.Loader: /home/photon/.virtualenvs/trydjango/local/lib/python2.7/site-packages/django/contrib/admin/templates/productss/detail.html
```
*Comes from the contrib/admin


```bash
django.template.loaders.app_directories.Loader: /home/photon/.virtualenvs/trydjango/local/lib/python2.7/site-packages/django/contrib/auth/templates/productss/detail.html
```
*Comes from the contrib/auth

## Django Forms ##
```bash
touch forms.py
```
forms.py
```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
```

views.py
```python
from .forms import ProductForm
def product_form_view(request, *args, **kwargs):
    form = ProductForm(requestPost or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'product_form_view.html', context)
```
products/product_form_view.html
```html
{% extends 'base.html' %}

{% block content %}
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save"/>
</form>
{% endblock %}
```

[trydjango] urls.py
```python
url(r'^product/create/', product_form_view, name="product_form_view")
```

## Creating Raw Django Form  ##
views.py
```python
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
```

forms.py
```python
class ProductRawForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    summary = forms.CharField()
    featured = forms.BooleanField()
```

[trydjango] urls.py
```python
    url(r'^product/rawcreate/', product_form_raw, name="product_form_raw")
```
## Form Widgets ##
forms.py
```python
    class ProductRawForm(forms.Form):
    title = forms.CharField(
                        label='', 
                        widget=forms.TextInput(
                            attrs= {
                                "placeholder": "Your title"
                            }
                        )
                    )
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "my-id-for-text-area",
                                "rows": 10,
                                "cols": 20
                            }
                        )
                    )
    price = forms.DecimalField(initial=12.99)
    summary = forms.CharField()
    featured = forms.BooleanField()
```

## Form Validation Methods ##
```python
class ProductForm(forms.ModelForm):
title = forms.CharField(
    label='',
    widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }
    )
)
class Meta:
    model = Product
    fields = [
        'title',
        'description',
        'price',
        'summary',
        'featured',
    ]
def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if not "Photon" in title:
        raise forms.ValidationError("This is not a valid title")
    return title

def clean_price(self, *args, **kwargs):
    price = self.cleaned_data.get("price")
    if price < 0:
        raise forms.ValidationError("This is not a valid number")
    return price
```

## Set Initial Data to the form ##
views.py
```python
def product_initial_data(request, *args, **kwargs):
    initial_data = {
        "title": "Initial Data"
    }
    obj = Product.objects.get(pk=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, 'products/product_initial_data.html', context)
```

## Dynamic URL Routing ##
urls.py
```python
    url(r'^product/dynamic-lookup/(?P<product_id>[0-9]+)/', dynamic_lookup_view, name="dynamic_look_view"),
```

views.py
```python
    def dynamic_lookup_view(request, product_id):
        obj = Product.objects.get(id=product_id)
        context = {
            "obj": obj
        }
        return render(request, "products/dynamic_lookup.html", context)

```

## Handle the Page that doesn't exist ##
views.py
```python
from django.shortcuts import render, get_object_or_404, Http404

def dynamic_lookup_view(request, product_id):
    obj = get_object_or_404(Product, id=product_id)
    # try:
    #     obj = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "obj": obj
    }
    return render(request, "products/dynamic_lookup.html", context)

```

## Delete a object in the database ##
views.py
```python
from django.shortcuts import redirect, get_object_or_404

def product_delete_view(request, product_id, *args, **kwargs):
    obj = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        obj.delete()
        return redirect("home/")
    context = {
        "obj": obj
    }
    return render(request, "products/product_delete.html", context)
```

urls.py
```python
url(r'^product/delete/(?P<product_id>[0-9]+)/', product_delete_view, name="product_delete_view")
```
products/product_delete.html
```html
{% extends 'base.html' %}

{% block content %}
<form action="." method="POST">
    {% csrf_token %}
    <h1> Do you want to delete the product {{ obj.title }}</h1>
    <p>
        <input type="submit" value="Yes"/>
        <a href="../">Cancel</a>
    </p>
</form>
{% endblock %}
```