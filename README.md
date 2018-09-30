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