from django.shortcuts import render

# Create your views here.
# Create your views here.


def home(request, *args, **kwargs):  # *args, **kwargs
    # print(args, kwargs) # see the wsgi requests
    #  (<WSGIRequest: GET '/'>,), {})

    # Therefore, we can see a request is coming
    # print(request.user) prints out the which user sent the request
    # Great for authentication, login

    # return HttpResponse("<h1>Hello World</h1>") #string of HTML Code
    return render(request, "pages/home.html", {})


def contact(request, *args, **kwargs):
    return render(request, "pages/contact.html", {})


def about(request, *args, **kwargs):
    context = {
        "address": [
            'Dhanmondi',
            'Gulshan',
            'Uttara'
        ]
    }
    return render(request, "pages/about.html", context)
