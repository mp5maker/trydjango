# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, "about.html", {}) 